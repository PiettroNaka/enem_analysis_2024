import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

class SamplingAnalysis:
    """Classe para análise de amostragem estatística."""
    
    def __init__(self, population_data, sample_size=None, confidence_level=0.95):
        """
        Inicializa a análise de amostragem.
        
        Parameters:
        -----------
        population_data : pd.DataFrame
            Dados da população
        sample_size : int, optional
            Tamanho da amostra. Se None, calcula baseado no nível de confiança
        confidence_level : float
            Nível de confiança (padrão: 0.95 = 95%)
        """
        self.population = population_data
        self.population_size = len(population_data)
        self.confidence_level = confidence_level
        
        # Calcula tamanho da amostra se não fornecido
        if sample_size is None:
            self.sample_size = self._calculate_sample_size()
        else:
            self.sample_size = sample_size
    
    def _calculate_sample_size(self, margin_of_error=0.05):
        """
        Calcula o tamanho da amostra usando a fórmula de Cochran.
        
        Parameters:
        -----------
        margin_of_error : float
            Margem de erro (padrão: 0.05 = 5%)
        
        Returns:
        --------
        int : Tamanho da amostra calculado
        """
        z_score = stats.norm.ppf((1 + self.confidence_level) / 2)
        p = 0.5  # Proporção máxima de variabilidade
        
        # Fórmula de Cochran
        n0 = (z_score ** 2 * p * (1 - p)) / (margin_of_error ** 2)
        
        # Ajuste para população finita
        n = n0 / (1 + (n0 - 1) / self.population_size)
        
        return int(np.ceil(n))
    
    def simple_random_sampling(self, seed=42):
        """
        Amostra Aleatória Simples.
        
        Returns:
        --------
        pd.DataFrame : Amostra aleatória simples
        """
        np.random.seed(seed)
        return self.population.sample(n=self.sample_size, random_state=seed)
    
    def systematic_sampling(self, seed=42):
        """
        Amostra Sistemática.
        
        Returns:
        --------
        pd.DataFrame : Amostra sistemática
        """
        np.random.seed(seed)
        k = self.population_size // self.sample_size
        start = np.random.randint(0, k)
        indices = np.arange(start, self.population_size, k)[:self.sample_size]
        return self.population.iloc[indices].reset_index(drop=True)
    
    def stratified_sampling(self, stratum_column, seed=42):
        """
        Amostra Estratificada.
        
        Parameters:
        -----------
        stratum_column : str
            Nome da coluna para estratificação
        
        Returns:
        --------
        pd.DataFrame : Amostra estratificada
        """
        np.random.seed(seed)
        
        # Calcula proporção de cada estrato
        strata = self.population[stratum_column].value_counts()
        strata_proportions = strata / len(self.population)
        
        # Aloca tamanho da amostra por estrato
        strata_sizes = (strata_proportions * self.sample_size).astype(int)
        
        # Coleta amostra de cada estrato
        samples = []
        for stratum, size in strata_sizes.items():
            stratum_data = self.population[self.population[stratum_column] == stratum]
            if len(stratum_data) > 0:
                sample = stratum_data.sample(n=min(size, len(stratum_data)), random_state=seed)
                samples.append(sample)
        
        return pd.concat(samples, ignore_index=True)
    
    def compare_samples(self, samples_dict, numeric_columns):
        """
        Compara estatísticas entre amostras e população.
        
        Parameters:
        -----------
        samples_dict : dict
            Dicionário com nome: amostra
        numeric_columns : list
            Colunas numéricas para comparação
        
        Returns:
        --------
        pd.DataFrame : Comparação de estatísticas
        """
        results = []
        
        # Estatísticas da população
        for col in numeric_columns:
            if col in self.population.columns:
                pop_data = self.population[col].dropna()
                if len(pop_data) > 0:
                    results.append({
                        'Grupo': 'População',
                        'Variável': col,
                        'Média': pop_data.mean(),
                        'Desvio Padrão': pop_data.std(),
                        'Mínimo': pop_data.min(),
                        'Máximo': pop_data.max(),
                        'Mediana': pop_data.median(),
                        'N': len(pop_data)
                    })
        
        # Estatísticas das amostras
        for sample_name, sample_df in samples_dict.items():
            for col in numeric_columns:
                if col in sample_df.columns:
                    sample_data = sample_df[col].dropna()
                    if len(sample_data) > 0:
                        results.append({
                            'Grupo': f'{sample_name}',
                            'Variável': col,
                            'Média': sample_data.mean(),
                            'Desvio Padrão': sample_data.std(),
                            'Mínimo': sample_data.min(),
                            'Máximo': sample_data.max(),
                            'Mediana': sample_data.median(),
                            'N': len(sample_data)
                        })
        
        return pd.DataFrame(results)


def calculate_frequency_distribution(series, bins=10):
    """
    Calcula distribuição de frequência.
    
    Parameters:
    -----------
    series : pd.Series
        Série de dados
    bins : int
        Número de bins para variáveis contínuas
    
    Returns:
    --------
    pd.DataFrame : Tabela de distribuição de frequência
    """
    if series.dtype == 'object' or series.nunique() < 20:
        # Variável qualitativa
        freq = series.value_counts()
        rel_freq = freq / len(series)
        cum_freq = freq.cumsum()
        cum_rel_freq = rel_freq.cumsum()
        
        df = pd.DataFrame({
            'Categoria': freq.index,
            'Frequência': freq.values,
            'Frequência Relativa': rel_freq.values,
            'Frequência Acumulada': cum_freq.values,
            'Frequência Relativa Acumulada': cum_rel_freq.values
        })
    else:
        # Variável quantitativa
        freq, bin_edges = np.histogram(series.dropna(), bins=bins)
        bin_labels = [f"{bin_edges[i]:.2f} - {bin_edges[i+1]:.2f}" for i in range(len(bin_edges)-1)]
        
        rel_freq = freq / len(series.dropna())
        cum_freq = np.cumsum(freq)
        cum_rel_freq = np.cumsum(rel_freq)
        
        df = pd.DataFrame({
            'Intervalo': bin_labels,
            'Frequência': freq,
            'Frequência Relativa': rel_freq,
            'Frequência Acumulada': cum_freq,
            'Frequência Relativa Acumulada': cum_rel_freq
        })
    
    return df


def identify_variable_types(df):
    """
    Identifica tipos de variáveis no dataframe.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataframe para análise
    
    Returns:
    --------
    dict : Dicionário com variáveis qualitativas e quantitativas
    """
    qualitative = []
    quantitative = []
    
    for col in df.columns:
        if df[col].dtype in ['object', 'category']:
            qualitative.append(col)
        elif df[col].dtype in ['int64', 'float64']:
            # Verifica se é realmente quantitativa
            if df[col].nunique() > 20:
                quantitative.append(col)
            else:
                qualitative.append(col)
    
    return {
        'qualitative': qualitative,
        'quantitative': quantitative
    }
