import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="ArtGallery",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "obras.csv"


# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1561214115-f2f134cc4912"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_ARTE = (
    "https://images.unsplash.com/"
    "photo-1549490349-8643362247b5"
    "?auto=format&fit=crop&w=1200&q=85"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =====================================================
   FUNDO
   ===================================================== */

.stApp {
    background:
        linear-gradient(
            135deg,
            #f7f1ff 0%,
            #eadcff 50%,
            #ddd6fe 100%
        );
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =====================================================
   SIDEBAR
   ===================================================== */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #170d24,
            #2b123f
        );

    border-right:
        2px solid #9333ea;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =====================================================
   LOGO
   ===================================================== */

.logo-title {
    font-size: 30px;
    font-weight: 800;
    color: #FFFFFF !important;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #d8b4fe !important;
    letter-spacing: 1px;
}


/* =====================================================
   TÍTULOS
   ===================================================== */

.page-title {
    font-size: 40px;
    font-weight: 800;
    color: #3b1763 !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #603b7c !important;
    margin-bottom: 30px;
}


/* =====================================================
   HERO
   ===================================================== */

.hero-container {
    position: relative;
    height: 420px;
    width: 100%;

    border-radius: 28px;
    overflow: hidden;

    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(70, 20, 100, 0.25);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(20, 8, 32, 0.96) 0%,
            rgba(40, 15, 60, 0.82) 45%,
            rgba(40, 15, 60, 0.15) 100%
        );
}

.hero-content {
    position: absolute;

    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 600px;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;

    color: #c084fc !important;

    line-height: 1;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;

    color: #FFFFFF !important;

    margin-top: 12px;

    line-height: 1.1;
}

.hero-text {
    font-size: 17px;

    color: #f3e8ff !important;

    margin-top: 20px;

    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #9333ea;

    color: #FFFFFF !important;

    font-size: 14px;

    font-weight: 700;
}


/* =====================================================
   CARDS
   ===================================================== */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid #d8b4fe;

    box-shadow:
        0 10px 25px rgba(70, 25, 100, 0.10);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 34px;

    font-weight: 800;

    color: #3b1763 !important;

    margin-top: 10px;
}

.card-label {
    font-size: 14px;

    font-weight: 700;

    color: #70469a !important;

    margin-top: 5px;
}


/* =====================================================
   CARD ESCURO
   ===================================================== */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #1a0c27,
            #32144b
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(45, 10, 70, 0.20);
}

.dark-card h2 {
    color: #FFFFFF !important;

    margin-top: 0;
}

.dark-card p {
    color: #eadcff !important;

    line-height: 1.7;
}


/* =====================================================
   FORMULÁRIO
   ===================================================== */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.90);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #c084fc;

    box-shadow:
        0 10px 30px rgba(70, 20, 100, 0.10);
}


/* =====================================================
   LABELS
   ===================================================== */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {

    color: #3b1763 !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}


/* =====================================================
   INPUTS
   ===================================================== */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {

    background-color:
        #FFFFFF !important;

    color:
        #26132f !important;

    -webkit-text-fill-color:
        #26132f !important;

    border:
        2px solid #a855f7 !important;

    border-radius:
        12px !important;

    font-size:
        16px !important;

    font-weight:
        500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {

    border:
        2px solid #7e22ce !important;

    box-shadow:
        0 0 0 3px rgba(126,34,206,0.15) !important;
}

input::placeholder,
textarea::placeholder {

    color:
        #80698f !important;

    opacity:
        1 !important;
}


/* =====================================================
   SELECTBOX
   ===================================================== */

[data-baseweb="select"] > div {

    background-color:
        #2b1838 !important;

    border:
        2px solid #9333ea !important;

    border-radius:
        12px !important;
}

[data-baseweb="select"] > div * {

    color:
        #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity:
        1 !important;
}

[data-baseweb="select"] input {

    color:
        #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] svg {

    fill:
        #FFFFFF !important;
}


/* =====================================================
   MENU DO SELECTBOX
   ===================================================== */

[data-baseweb="popover"] {
    background-color:
        #2b1838 !important;
}

[data-baseweb="menu"] {
    background-color:
        #2b1838 !important;
}

[role="option"] {

    background-color:
        #2b1838 !important;

    color:
        #FFFFFF !important;
}

[role="option"]:hover {

    background-color:
        #7e22ce !important;

    color:
        #FFFFFF !important;
}


/* =====================================================
   BOTÕES
   ===================================================== */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {

    background:
        linear-gradient(
            135deg,
            #7e22ce,
            #a855f7
        ) !important;

    color:
        #FFFFFF !important;

    border:
        none !important;

    border-radius:
        14px !important;

    min-height:
        54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size:
        15px !important;

    font-weight:
        700 !important;

    box-shadow:
        0 8px 18px rgba(126,34,206,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {

    background:
        linear-gradient(
            135deg,
            #6b21a8,
            #9333ea
        ) !important;

    color:
        #FFFFFF !important;

    transform:
        translateY(-1px);
}


/* =====================================================
   TABELA
   ===================================================== */

[data-testid="stDataFrame"] {

    background:
        #FFFFFF;

    border-radius:
        18px;

    overflow:
        hidden;

    border:
        1px solid #c084fc;
}


/* =====================================================
   RODAPÉ
   ===================================================== */

.footer {

    margin-top:
        50px;

    text-align:
        center;

    color:
        #70469a !important;

    font-size:
        14px;

    font-weight:
        600;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Obra",
        "Artista",
        "Ano",
        "Tecnica",
        "Categoria",
        "Descricao"
    ]

    if os.path.exists(ARQUIVO):

        try:
            return pd.read_csv(ARQUIVO)

        except Exception:
            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# =========================================================
# GARANTIR COLUNAS
# =========================================================

colunas_necessarias = [
    "Obra",
    "Artista",
    "Ano",
    "Tecnica",
    "Categoria",
    "Descricao"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:
        df[coluna] = ""


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
🎨 ArtGallery
</div>

<div class="logo-subtitle">
ARTE, CRIATIVIDADE E EXPRESSÃO
</div>
""",
unsafe_allow_html=True
)

st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)

menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Obra",
        "🖼️ Obras Cadastradas"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "ArtGallery • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Sua arte.<br>
Sua expressão.
</div>

<div class="hero-text">

Organize suas obras de arte,
artistas e técnicas em um único lugar.

Cadastre, pesquise e acompanhe
sua coleção artística de forma simples
e organizada.

</div>

<div class="hero-badge">
🎨 GALERIA DIGITAL
</div>

</div>

</div>
""",
unsafe_allow_html=True
)


    st.markdown(
"""
<div class="page-title">
🖼️ Sua galeria de arte
</div>

<div class="page-subtitle">
Veja um resumo das obras cadastradas no ArtGallery.
</div>
""",
unsafe_allow_html=True
)


    total_obras = len(df)

    total_artistas = (
        df["Artista"]
        .replace("", pd.NA)
        .dropna()
        .nunique()
    )

    total_tecnicas = (
        df["Tecnica"]
        .replace("", pd.NA)
        .dropna()
        .nunique()
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🎨
</div>

<div class="card-number">
{total_obras}
</div>

<div class="card-label">
OBRAS CADASTRADAS
</div>

</div>
""",
unsafe_allow_html=True
)


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
👩‍🎨
</div>

<div class="card-number">
{total_artistas}
</div>

<div class="card-label">
ARTISTAS
</div>

</div>
""",
unsafe_allow_html=True
)


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
🖌️
</div>

<div class="card-number">
{total_tecnicas}
</div>

<div class="card-label">
TÉCNICAS
</div>

</div>
""",
unsafe_allow_html=True
)


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
✨ Arte em um só lugar
</h2>

<p>
O ArtGallery foi desenvolvido para
organizar obras de arte de maneira
simples, bonita e prática.
</p>

<p>
Cadastre suas obras, artistas e técnicas,
pesquise sua coleção e mantenha todas
as informações organizadas em um único lugar.
</p>

</div>
""",
unsafe_allow_html=True
)


    with coluna2:

        st.image(
            IMAGEM_ARTE,
            use_container_width=True
        )


# =========================================================
# CADASTRAR OBRA
# =========================================================

elif menu == "➕ Cadastrar Obra":

    st.markdown(
"""
<div class="page-title">
➕ Nova obra
</div>

<div class="page-subtitle">
Adicione uma nova obra à sua galeria.
</div>
""",
unsafe_allow_html=True
)


    with st.form(
        "cadastro_obra",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            obra = st.text_input(
                "🎨 Nome da obra"
            )

            artista = st.text_input(
                "👩‍🎨 Artista"
            )

            ano = st.number_input(
                "📅 Ano",
                min_value=1000,
                max_value=2035,
                value=2024,
                step=1
            )


        with col2:

            tecnica = st.selectbox(
                "🖌️ Técnica",
                [
                    "Desenho",
                    "Pintura",
                    "Aquarela",
                    "Arte digital",
                    "Fotografia",
                    "Escultura",
                    "Colagem",
                    "Gravura",
                    "Outra"
                ]
            )

            categoria = st.selectbox(
                "🗂️ Categoria",
                [
                    "Retrato",
                    "Paisagem",
                    "Abstrato",
                    "Natureza",
                    "Arte contemporânea",
                    "Ilustração",
                    "Fanart",
                    "Outro"
                ]
            )

            descricao = st.text_area(
                "📝 Descrição",
                placeholder="Descreva brevemente a obra..."
            )


        cadastrar = st.form_submit_button(
            "💾 CADASTRAR OBRA"
        )


    if cadastrar:

        if (
            obra.strip()
            and artista.strip()
        ):

            nova_obra = pd.DataFrame(
                [{
                    "Obra": obra.strip(),
                    "Artista": artista.strip(),
                    "Ano": int(ano),
                    "Tecnica": tecnica,
                    "Categoria": categoria,
                    "Descricao": descricao.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    nova_obra
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "🎨 Obra cadastrada com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha o nome da obra e o artista."
            )


# =========================================================
# OBRAS CADASTRADAS
# =========================================================

elif menu == "🖼️ Obras Cadastradas":

    st.markdown(
"""
<div class="page-title">
🖼️ Minha galeria
</div>

<div class="page-subtitle">
Consulte e pesquise suas obras cadastradas.
</div>
""",
unsafe_allow_html=True
)


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
🎨 Nenhuma obra cadastrada
</h2>

<p>
Sua galeria ainda está vazia.
Cadastre sua primeira obra para começar.
</p>

</div>
""",
unsafe_allow_html=True
)


    else:

        busca = st.text_input(
            "🔎 Pesquisar obra",
            placeholder="Digite obra, artista, técnica ou categoria..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False,
                        regex=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        opcoes_obras = df.index.tolist()


        obra_excluir = st.selectbox(
            "🗑️ Selecione uma obra para excluir",
            options=opcoes_obras,
            format_func=lambda indice:
                f"{df.loc[indice, 'Obra']} - "
                f"{df.loc[indice, 'Artista']}"
        )


        if st.button(
            "🗑️ EXCLUIR OBRA"
        ):

            df = df.drop(
                obra_excluir
            )


            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "🎨 Obra excluída com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

🎨 ArtGallery<br>
Arte, criatividade e expressão.

</div>
""",
unsafe_allow_html=True
)
