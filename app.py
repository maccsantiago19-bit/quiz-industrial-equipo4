import streamlit as st
import random

st.set_page_config(page_title="Quiz Productividad", page_icon="📊")

# ---------------- PREGUNTAS ----------------
preguntas_base = [
    {
        "pregunta": "¿Qué es un tiempo estándar?",
        "opciones": [
            "Tiempo promedio sin método definido",
            "Tiempo establecido para realizar una operación bajo condiciones normales",
            "Tiempo máximo permitido por el supervisor"
        ],
        "correcta": "Tiempo establecido para realizar una operación bajo condiciones normales"
    },
    {
        "pregunta": "La eficiencia se calcula como:",
        "opciones": [
            "Producción real / Producción esperada",
            "Tiempo muerto / Tiempo total",
            "Horas trabajadas / Horas pagadas"
        ],
        "correcta": "Producción real / Producción esperada"
    },
    {
        "pregunta": "¿Qué indica la capacidad productiva?",
        "opciones": [
            "El número de empleados",
            "La cantidad máxima que se puede producir en un periodo",
            "La velocidad de una máquina"
        ],
        "correcta": "La cantidad máxima que se puede producir en un periodo"
    },
    {
        "pregunta": "Un tiempo muerto es:",
        "opciones": [
            "Tiempo sin producción por causas no planeadas",
            "Tiempo de descanso programado",
            "Tiempo de capacitación"
        ],
        "correcta": "Tiempo sin producción por causas no planeadas"
    },
    {
        "pregunta": "Si la eficiencia es mayor a 100% significa:",
        "opciones": [
            "Se produjo más de lo esperado",
            "Se produjo menos",
            "No hubo producción"
        ],
        "correcta": "Se produjo más de lo esperado"
    },
    {
        "pregunta": "La capacidad productiva depende de:",
        "opciones": [
            "Máquinas, personal y tiempo disponible",
            "Solo del supervisor",
            "Solo del turno nocturno"
        ],
        "correcta": "Máquinas, personal y tiempo disponible"
    },
    {
        "pregunta": "Un estudio de tiempos sirve para:",
        "opciones": [
            "Definir estándares de producción",
            "Reducir salarios",
            "Aumentar descansos"
        ],
        "correcta": "Definir estándares de producción"
    },
    {
        "pregunta": "La productividad aumenta cuando:",
        "opciones": [
            "Se producen más unidades con los mismos recursos",
            "Se trabaja menos tiempo",
            "Hay más descansos"
        ],
        "correcta": "Se producen más unidades con los mismos recursos"
    },
    {
        "pregunta": "El tiempo ciclo es:",
        "opciones": [
            "Tiempo de inicio de turno",
            "Tiempo total para completar una operación",
            "Tiempo de comida"
        ],
        "correcta": "Tiempo total para completar una operación"
    },
    {
        "pregunta": "Un indicador de productividad mide:",
        "opciones": [
            "Relación entre producción y recursos utilizados",
            "Horas extras",
            "Número de supervisores"
        ],
        "correcta": "Relación entre producción y recursos utilizados"
    },
]

# ---------------- FUNCIONES ----------------
def generar_quiz():
    preguntas = random.sample(preguntas_base, 10)
    for p in preguntas:
        random.shuffle(p["opciones"])
    return preguntas

# ---------------- SESSION STATE ----------------
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "quiz" not in st.session_state:
    st.session_state.quiz = generar_quiz()
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}
if "finalizado" not in st.session_state:
    st.session_state.finalizado = False

# ---------------- UI ----------------
st.title("Quiz de Productividad y Tiempos")

# Registro de nombre
if st.session_state.nombre == "":
    nombre = st.text_input("Ingresa tu nombre:")
    if st.button("Comenzar Quiz"):
        if nombre.strip() != "":
            st.session_state.nombre = nombre
            st.rerun()
        else:
            st.warning("Debes ingresar un nombre")
    st.stop()

st.write(f"Participante: **{st.session_state.nombre}**")

# Mostrar preguntas
if not st.session_state.finalizado:
    for i, p in enumerate(st.session_state.quiz):
        st.subheader(f"Pregunta {i+1}")
        opcion = st.radio(
            p["pregunta"],
            p["opciones"],
            key=f"pregunta_{i}"
        )
        st.session_state.respuestas[i] = opcion

    if st.button("Finalizar Quiz"):
        st.session_state.finalizado = True
        st.rerun()

# Resultados
if st.session_state.finalizado:
    puntos = 0
    for i, p in enumerate(st.session_state.quiz):
        if st.session_state.respuestas.get(i) == p["correcta"]:
            puntos += 1

    calificacion = (puntos / 10) * 10

    st.success(f"Puntos obtenidos: {puntos}/10")
    st.info(f"Calificación final: {calificacion:.1f} / 10")

    if st.button("Reiniciar Quiz"):
        st.session_state.quiz = generar_quiz()
        st.session_state.respuestas = {}
        st.session_state.finalizado = False
        st.session_state.nombre = ""
        st.rerun()
