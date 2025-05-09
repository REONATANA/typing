from flask import Flask, render_template, request
import random

app = Flask(__name__)

SENTENCESJP = [
"attend",  
"employee",  
"address",
"computer",  
"travel",  
"business",  
"report",  
"contact",  
"office",  
"arrive", 
"project",  
"call"  ,
"finish" , 
"meeting" , 
"manager"  ,
"schedule"  ,
"agree"  ,
"lunch"  ,
"customer",  
"price"  ,
"close"  ,
"benefit" , 
"complete" , 
"company"  ,
"important" , 
"conference" , 
"document"  ,
"store"  ,
"event"  ,
"send"  ,
"available"  ,
"change"  ,
"check"  ,
"daily"  ,
"deliver"  ,
"department",  
"develop"  ,
"discount"  ,
"download"  ,
"drive"  ,
"email"  ,
"energy"  ,
"enjoy"  ,
"enter"  ,
"equipment",  
"every"  ,
"example"  ,
"expert"  ,
"fail"  ,
"famous" , 
"fast"  ,
"feel"  ,
"file"  ,
"final"  ,
"floor"  ,
"follow"  ,
"free"  ,
"full"  ,
"future" , 
"hand"  ,
"hard"  ,
"help"  ,
"hold"  ,
"hotel"  ,
"idea"  ,
"include",  
"information"  
"job"  ,
"keep"  ,
"know"  ,
"learn"  ,
"leave"  ,
"line"  ,
"list"  ,
"local"  ,
"lose"  ,
"low"  ,
"main"  ,
"make"  ,
"manager",  
"market"  ,
"material" , 
"meeting"  ,
"money"  ,
"need"  ,
"note"  ,
"offer"  ,
"open"  ,
"order"  ,
"paper"  ,
"pay"  ,
"plan"  ,
"present",  
"print"  ,
"product" , 
"receive"  ,
"room"  ,
"sale"  ,
"service",  
"staff"  ,
"start"  ,
"stay"  ,
"success",  
"system"  ,
"take"  ,
"talk"  ,
"team"  ,
"ticket"
]

SENTENCESEN = [
    "accomplish",
    "accurate",
    "acknowledge",
    "acquire",
    "adapt",
    "adjust",
    "administration",
    "agenda",
    "allocate"
    "analyze",
    "anticipate",
    "applicant",
    "appreciate",
    "appropriate",
    "approve",
    "assemble",
    "assess",
    "assign",
    "assistance",
    "assume",
    "assure",
    "attach",
    "attain",
    "attribute",
    "authorize",
    "automate",
    "availability",
    "aware",
    "barrier",
    "beneficial",
    "budget",
    "cancellation",
    "capacity",
    "certification",
    "clarify",
    "collaborate",
    "commence",
    "commitment",
    "commodity",
    "compensation",
    "competent",
    "compile",
    "comply",
    "comprehensive",
    "compromise",
    "conceive",
    "conclude",
    "concurrent",
    "conduct",
    "confidential",
    "consecutive",
    "consensus",
    "consolidate",
    "constraint",
    "consult",
    "consume",
    "contingency",
    "contractor",
    "contribute",
    "controversial",
    "convene",
    "coordinate",
    "correspond",
    "criterion",
    "crucial",
    "dedicate",
    "deficiency",
    "delegate",
    "deliberate",
    "demonstrate",
    "denote",
    "depreciation",
    "derivative",
    "designate",
    "determine",
    "devise",
    "diagnose",
    "diligent",
    "discrepancy",
    "disseminate",
    "distinguish",
    "diversify",
    "dominant",
    "economical",
    "elaborate",
    "eliminate",
    "emphasize",
    "encompass",
    "enhance",
    "enroll",
    "ensure",
    "entail",
    "entrepreneur",
    "equivalent",
    "evaluate",
    "exceed",
    "exclusive",
    "execute",
    "exemplify",
    "exhaustive",
    "expenditure",
    "expertise",
    "explicit",
    "exploit",
    "facilitate",
    "feasible",
    "fluctuate",
    "formulate",
    "foster",
    "framework",
    "fulfill",
    "generate",
    "guideline",
    "hierarchy",
    "hypothesis",
    "illustrate",
    "implement",
    "implication",
    "impose",
    "incentive",
    "incorporate",
    "indicate",
    "induce",
    "inevitable",
    "infer",
    "infrastructure",
    "inhibit",
    "initiate",
    "innovate",
    "insight",
    "inspection",
    "integrate",
    "integrity",
    "intervene",
    "intuitive",
    "inventory",
    "investigate",
    "invoke",
    "justify",
    "legitimate",
    "liaison",
    "litigation",
    "maintain",
    "mandatory",
    "manipulate",
    "mechanism",
    "mediate",
    "meticulous",
    "mitigate",
    "moderate",
    "monetary",
    "negotiate",
    "nominate",
    "obligation",
    "obtain",
    "offset",
    "omit",
    "ongoing",
    "optimize",
    "orient",
    "outcome",
    "oversee",
    "paradigm",
    "parameter",
    "participate",
    "perceive",
    "permanent",
    "persist",
    "perspective",
    "pertinent",
    "pioneer",
    "plausible",
    "policy",
    "portion",
    "pragmatic",
    "precede",
    "precise",
    "predominant",
    "preliminary",
    "presume",
    "prevail",
    "priority",
    "proceed",
    "proficient",
    "prohibit",
    "prominent",
    "promote",
    "prone",
    "proportion",
    "prospective",
    "protocol",
    "provision",
    "qualitative",
    "quantitative",
    "quintessential",
    "reciprocal",
    "recommendation",
    "reconcile",
    "redundant",
    "refine",
    "reflect",
    "regulate",
    "reinforce",
    "reiterate",
    "relevant",
    "reluctant",
    "rely",
    "remedy",
    "renovate",
    "requisite",
    "reside",
    "resolve",
    "respective",
    "restrict",
    "retain",
    "revenue",
    "rigorous",
    "safeguard",
    "scrutinize",
    "simulate",
    "simultaneous",
    "sophisticated",
    "specific",
    "sponsor",
    "spontaneous",
    "stagnant",
    "strategic",
    "subordinate",
    
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/typing")
def typing():
    mode = request.args.get("mode", "jp")
    if mode == "en":
        sentence = random.choice(SENTENCESEN)
    else:
        sentence = random.choice(SENTENCESJP)
    return render_template("typing.html", sentence=sentence, mode=mode)

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/stats")
def stats():
    return render_template("stats.html")

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # ← Renderが指定するPORTを使う
    app.run(host='0.0.0.0', port=port)
