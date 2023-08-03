from django.db.models import TextChoices


class ChoicesCategoriaManutencao(TextChoices):
    ALINHAMENTO_BALANCEAMENTO = 'AB', 'Alinhamento e Balanceamento'
    DIAGNOSTICO_ELETRONICO = 'DE', 'Diagnóstico Eletrônico'
    LIMPEZA_AR_CONDICIONADO = 'LAC', 'Limpeza do Sistema de Ar Condicionado'
    LIMPEZA_BICOS_INJETORES = 'LBI', 'Limpeza de Bicos Injetores'
    LIMPEZA_RADIADOR = 'LR', 'Limpeza do Radiador'
    RECARGA_AR_CONDICIONADO = 'RAC', 'Recarga do Sistema de Ar Condicionado'
    REPARO_SISTEMA_FREIOS = 'RSF', 'Reparo no Sistema de Freios'
    REVISAO_PREVENTIVA = 'RP', 'Revisão Preventiva'
    TROCAR_ACEITE_DIFERENCIAL = 'TAD', 'Troca do Óleo do Diferencial'
    TROCAR_AMORTECEDORES = 'TA', 'Troca de Amortecedores'
    TROCAR_BATERIA = 'TB', 'Troca da Bateria'
    TROCAR_CORREIA_ALTERNADOR = 'TCA', 'Troca da Correia do Alternador'
    TROCAR_CORREIA_DENTADA = 'TCD', 'Troca da Correia Dentada'
    TROCAR_FILTRO_AR = 'TFA', 'Troca do Filtro de Ar'
    TROCAR_FILTRO_COMBUSTIVEL = 'TFC', 'Troca do Filtro de Combustível'
    TROCAR_FLUIDO_FREIOS = 'TFF', 'Troca de Fluido de Freios'
    TROCAR_KIT_EMBREAGEM = 'TKE', 'Troca do Kit de Embreagem'
    TROCAR_OLEO = 'TO', 'Troca de Óleo'
    TROCAR_PASTILHAS_FREIO = 'TPF', 'Troca de Pastilhas de Freio'
    TROCAR_VELAS_IGNICAO = 'TVI', 'Troca de Velas de Ignição'
