# Definición de categorías y variables (con sinónimos unificados)
CATEGORIAS = {
    "Habilidades": [
        "Abstraction", "Algorithm", "Algorithmic thinking", "Coding", "Collaboration", "Cooperation",
        "Creativity", "Critical thinking", "Debug", "Decomposition", "Evaluation", "Generalization",
        "Logic", "Logical thinking", "Modularity", "Patterns recognition", "Problem solving",
        "Programming", "Representation", "Reuse", "Simulation"
    ],
    "Conceptos Computacionales": [
        "Conditionals", "Control structures", "Directions", "Events", "Functions", "Loops",
        "Modular structure", "Parallelism", "Sequences", "Software/hardware", "Variables"
    ],
    "Actitudes": [
        "Emotional engagement", "Motivation", "Perceptions", "Persistence", "Self-efficacy",
        "Self-perceived"
    ],
    "Propiedades Psicométricas": [
        "Classical Test Theory - CTT", "Confirmatory Factor Analysis - CFA",
        "Exploratory Factor Analysis - EFA", "Item Response Theory (IRT) - IRT", "Reliability",
        "Structural Equation Model - SEM", "Validity"
    ],
    "Herramienta de Evaluación": [
        "Beginners Computational Thinking test - BCTt", "Coding Attitudes Survey - ESCAS",
        "Collaborative Computing Observation Instrument", "Competent Computational Thinking test - cCTt",
        "Computational thinking skills test - CTST", "Computational concepts",
        "Computational Thinking Assessment for Chinese Elementary Students - CTA-CES",
        "Computational Thinking Challenge - CTC", "Computational Thinking Levels Scale - CTLS",
        "Computational Thinking Scale - CTS", "Computational Thinking Skill Levels Scale - CTS",
        "Computational Thinking Test - CTt", "Computational Thinking Test",
        "Computational Thinking Test for Elementary School Students - CTT-ES",
        "Computational Thinking Test for Lower Primary - CTtLP",
        "Computational thinking-skill tasks on numbers and arithmetic",
        "Computerized Adaptive Programming Concepts Test - CAPCT", "CT Scale - CTS",
        "Elementary Student Coding Attitudes Survey - ESCAS", "General self-efficacy scale",
        "ICT competency test", "Instrument of computational identity",
        "KBIT fluid intelligence subtest", "Mastery of computational concepts Test and an Algorithmic Test",
        "Multidimensional 21st Century Skills Scale", "Self-efficacy scale",
        "STEM learning attitude scale - STEM-LAS", "The computational thinking scale"
    ],
    "Diseño de Investigación": [
        "No experimental", "Experimental", "Longitudinal research", "Mixed methods",
        "Post-test", "Pre-test", "Quasi-experiments"
    ],
    "Nivel de Escolaridad": [
        "Upper elementary education - Upper elementary school",
        "Primary school - Primary education - Elementary school",
        "Early childhood education - Kindergarten - Preschool",
        "Secondary school - Secondary education", "High school - Higher education",
        "University - College"
    ],
    "Medio": [
        "Block programming", "Mobile application", "Pair programming", "Plugged activities",
        "Programming", "Robotics", "Spreadsheet", "STEM", "Unplugged activities"
    ],
    "Estrategia": [
        "Construct-by-self mind mapping - CBS-MM", "Construct-on-scaffold mind mapping - COS-MM",
        "Design-based learning - CTDBL", "Design-based learning - DBL",
        "Evidence-centred design approach", "Gamification", "Reverse engineering pedagogy - REP",
        "Technology-enhanced learning", "Collaborative learning", "Cooperative learning",
        "Flipped classroom", "Game-based learning", "Inquiry-based learning", "Personalized learning",
        "Problem-based learning", "Project-based learning", "Universal design for learning"
    ],
    "Herramienta": [
        "Alice", "Arduino", "Scratch", "ScratchJr", "Blockly Games", "Code.org", "Codecombat",
        "CSUnplugged", "Robot Turtles", "Hello Ruby", "Kodable", "LightbotJr", "KIBO robots",
        "BEE BOT", "CUBETTO", "Minecraft", "Agent Sheets", "Mimo", "Py– Learn", "SpaceChem"
    ]
}
def obtener_categorias():
    return list(CATEGORIAS.keys())
