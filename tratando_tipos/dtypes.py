import pandas as pd

def otimizar_df(df):

    """
    Essa Função faz um Downcast em todo o DataFrame colocando apenas os tipos necessários
    para aquele DataFrame.
    """

    # Auditoria Inicial
    print("--- MEMÓRIA ORIGINAL ---")
    mem_inicial = df.memory_usage(deep=True).sum()
    print(f"Total: {mem_inicial / 1024**2:.2f} MB")

    for col in df.columns:
        col_type = df[col].dtype
        
        # Se for numérico
        if col_type != object and col_type.name != 'category':
            # Tenta reduzir Inteiro ou Float
            if 'int' in col_type.name:
                df[col] = pd.to_numeric(df[col], downcast='integer')
            else:
                df[col] = pd.to_numeric(df[col], downcast='float')
        
        # Se for texto (Object)
        else:
            # Se mais de 50% dos valores forem repetidos, vira categoria
            num_unique = len(df[col].unique())
            num_total = len(df[col])
            if num_unique / num_total < 0.5:
                df[col] = df[col].astype('category')

    # Auditoria Final
    print("\n--- MEMÓRIA PÓS-OTIMIZAÇÃO ---")
    mem_final = df.memory_usage(deep=True).sum()
    print(f"Total: {mem_final / 1024**2:.2f} MB")

    # Para ver a redução de Memória
    reducao = (1 - (mem_final / mem_inicial)) * 100
    print(f"Redução de {reducao:.2f}%! Sensacional.")