from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class AddFeatures(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        df = X.copy()
        df["avg_humanas"] = df[["NOTA_DE", "NOTA_EM", "NOTA_GO", "INGLES"]].mean(axis=1)
        df["reprovacoes_total"] = df[["REPROVACOES_DE", "REPROVACOES_EM", "REPROVACOES_MF", "REPROVACOES_GO"]].mean(axis=1)
        df["study_volume"] = df["H_AULA_PRES"] * df["TAREFAS_ONLINE"]
        # Retornamos um novo dataframe sem as colunas indesejadas
        return df
