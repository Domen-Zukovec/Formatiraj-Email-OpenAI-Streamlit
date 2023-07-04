import streamlit as st
from langchain import PromptTemplate
from langchain.llms import AzureOpenAI

import os

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = "https://domzisopenai.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "3673181a896c4997baba06bc82db5e6f"

template = """
Below is an email that may be poorly worded.
Your goal is to:
- Properly format the email
- Write it in {language} or if needed translate it to {language}
- Write in {tone} style

EMAIL: {email}

PROPERLY FORMATED EMAIL:
"""

prompt = PromptTemplate(
    input_variables=["tone", "language", "email"],
    template=template,
)

def load_LMM():
    llm = AzureOpenAI( 
        deployment_name="TextDavinci003",
        model_name="text-davinci-002",
    )
    return llm

llm = load_LMM()

st.set_page_config(page_title="Formaliziraj email")
st.header("Formaliziraj email")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Ste kdaj želeli, da bi vaša elektronska sporočila delovala bolj profesionalno, a niste vedeli, kako to doseči? Imamo pravo rešitev za vas!\n\nNaše revolucionarno orodje spreminja način komuniciranja v poslovnem svetu, tako da vaše običajne emaile preoblikuje v mojstrovine formalne korespondence. Zdaj lahko v vsakem trenutku izražate svoje misli z jasnostjo in prepričljivostjo, ki jo pričakuje poslovni svet.\n\nNe dovolite, da vas omejujejo nezadostne veščine pisanja - z našim orodjem postane pisanje profesionalnih emailov preprosto, učinkovito in brez napora. Začnite danes in opazujte, kako se vaša poslovna komunikacija dviga na popolnoma novo raven! Made by: @Domen_Žukovec")

with col2:
    st.image(image="pic.jpg", width=210, caption="www.comtrade.si")

st.markdown("## Vpišite svoj email")

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox(
        'V kakšnem slogu želite spisan email?',
        ('Formalen', 'Pogovoren')
    )

with col2:
    option_language = st.selectbox(
        'V katerem jeziku je email?',
        ('Slovenščina', 'English')
    )

def get_text():
    input_text = st.text_area(label="", placeholder="Your Email...", key="email_input")
    return input_text

email_input = get_text()

st.markdown("## Vaš transformiran email:")


if email_input:
    
    if option_language == "English":
        if option_tone == "Formalen":
            selected_tone = "formal"
        else:
            selected_tone = "informal"
    else:
        if option_tone == "Formalen":
            selected_tone = "formalenem"
        else:
            selected_tone = "pogovorenem"

    prompt_with_input_values = prompt.format(tone=selected_tone, language=option_language, email=email_input)

    formatted_email = llm(prompt_with_input_values)

    st.write(formatted_email)