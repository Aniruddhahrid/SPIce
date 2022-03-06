from flask import Flask
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

phy12 = ["ELECTRIC CHARGES AND FIELDS",
         "ELECTROSTATIC POTENTIAL AND CAPACITANCE",
         "CURRENT ELECTRICITY",
         "MOVING CHARGES AND MAGNETISM",
         "MAGNETISM AND MATTER",
         "ELECTROMAGNETIC INDUCTION",
         "ALTERNATING CURRENT",
         "ELECTROMAGNETIC WAVES",
         "RAY OPTICS AND OPTICAL INSTRUMENTS",
         "WAVE OPTICS",
         "DUAL NATURE OF RADIATION AND MATTER",
         "ATOMS",
         "NUCLEI",
         "SEMICONDUCTOR ELECTRONICS: MATERIALS, DEVICES AND SIMPLE CIRCUITS"]

phy11 = ["PHYSICAL WORLD",
         "UNITS AND MEASUREMENTS",
         "MOTION IN A STRAIGHT LINE",
         "MOTION IN A PLANE",
         "LAWS OF MOTION",
         "WORK, ENERGY AND POWER",
         "SYSTEM OF PARTICLES AND ROTATIONAL MOTION",
         "GRAVITATION",
         "MECHANICAL PROPERTIES OF SOLIDS",
         "MECHANICAL PROPERTIES OF FLUIDS",
         "THERMAL PROPERTIES OF MATTER",
         "THERMODYNAMICS",
         "KINETIC THEORY",
         "OSCILLATIONS",
         "WAVES"]

che11 = ["Some Basic Concepts of Chemistry",
         "Structure of Atom",
         "Classification of Elements and Periodicity in Properties",
         "Chemical Bonding and Molecular Structure",
         "States of Matter",
         "Thermodynamics",
         "Equilibrium",
         "Redox Reactions",
         "Hydrogen",
         "The s-Block Elements",
         "The p-Block Elements",
         "Organic Chemistry -- Some Basic Principles and Techniques",
         "Hydrocarbons",
         "Environmental Chemistry"]

che12 = ["The Solid State",
         "Solutions",
         "Electrochemistry",
         "Chemical Kinetics",
         "Surface Chemistry",
         "General Principles and Processes of Isolation of Elements",
         "The p-Block Elements",
         "The d-and f-Block Elements",
         "Coordination Compounds ",
         "Haloalkanes and Haloarenes",
         "Alcohols, Phenols and Ethers",
         "Aldehydes, Ketones and Carboxylic Acids",
         "Amines",
         "Biomolecules",
         "Polymers",
         "Chemistry in Everyday Life"]

math11 = ["Sets",
          "Relations and Functions",
          "Trigonometric Functions",
          "Principle of Mathematical Induction",
          "Complex Numbers and Quadratic Equations",
          "Linear Inequalities",
          "Permutations and Combinations",
          "Binomial Theorem",
          "Sequences and Series",
          "Straight Lines",
          "Conic Sections",
          "Introduction to Three Dimensional Geometry ",
          " Limits and Derivatives ",
          "Mathematical Reasoning",
          "Statistics",
          "Probability"]

math12 = ["Relations and Functions",
          "Inverse Trigonometric Functions",
          "Matrices",
          "Determinants",
          "Continuity and Differentiability",
          "Application of Derivatives",
          "Integrals",
          "Application of Integrals",
          "Differential Equations",
          "Vector Algebra",
          "Three Dimensional Geometry",
          "Linear Programming",
          "Probability"]


def getDay(dt):
    year, month, day = (int(x) for x in dt.split('-'))
    ans = datetime.date(year, month, day)
    return (ans.strftime("%A"))


days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']


@app.route('/')
def homePage():
    return "Hello"


@app.route('/chem12chapters')
def getChem12Chapters():
    totalChem12Chapters = len(che12)
    StrDates = getDates(totalChem12Chapters)
    data_set = {"jsonStrChapters": che12, "jsonStrDates": StrDates}
    return data_set


@app.route('/chem11chapters')
def getChem11Chapters():
    totalChem11Chapters = len(che11)
    StrDates = getDates(totalChem11Chapters)
    data_set = {"jsonStrChapters": che11, "jsonStrDates": StrDates}
    return data_set


@app.route('/phy12chapters')
def getPhy12Chapters():
    totalPhy12Chapters = len(phy12)
    StrDates = getDates(totalPhy12Chapters)
    data_set = {"jsonStrChapters": phy12, "jsonStrDates": StrDates}
    return data_set


@app.route('/phy11chapters')
def getPhy11Chapters():
    totalPhy11Chapters = len(phy11)
    StrDates = getDates(totalPhy11Chapters)
    data_set = {"jsonStrChapters": phy11, "jsonStrDates": StrDates}
    return data_set


@app.route('/math12chapters')
def getMath12Chapters():
    totalMath12Chapters = len(math12)
    StrDates = getDates(totalMath12Chapters)
    data_set = {"jsonStrChapters": math12, "jsonStrDates": StrDates}
    return data_set


@app.route('/math11chapters')
def getMath11Chapters():
    totalMath11Chapters = len(math11)
    StrDates = getDates(totalMath11Chapters)
    data_set = {"jsonStrChapters": math11, "jsonStrDates": StrDates}
    return data_set


# @app.route('/chem12dates')
# def getChem12Dates():
#     totalChem12Chapters = len(che12)
#     return getDates(totalChem12Chapters)


# @app.route('/chem11chapters')
# def getChem11Chapters():
#     jsonStr = json.dumps(che11)
#     return jsonStr


# @app.route('/phy12chapters')
# def getPhy12Chapters():
#     jsonStr = json.dumps(phy12)
#     return jsonStr


# @app.route('/phy11chapters')
# def getPhy11Chapters():
#     jsonStr = json.dumps(phy11)
#     return jsonStr


# @app.route('/math12chapters')
# def getMath12Chapters():
#     jsonStr = json.dumps(math12)
#     return jsonStr


# @app.route('/math11chapters')
# def getMath11Chapters():
#     jsonStr = json.dumps(math11)
#     return jsonStr


def getDates(num):
    dates = []
    for i in range(0, num):
        x = str(datetime.datetime.now() + datetime.timedelta(days=i))[:10]
        dates.append((x+getDay(x)))
    return dates


app.run(host='0.0.0.0', port=5000)
