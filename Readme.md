# Gentzen's Proof Tree

---

## Following are my details for assignment submission:
<p>Name: &nbsp;&nbsp;&nbsp;&nbsp;Sakshi Shashikant Yeole</p>
<p>Roll No.: &nbsp;20CS01047</p>
<p>Semester: &nbsp;7</p>
<p>Year of study: &nbsp;4th year</p>
<p>Subject: &nbsp;&nbsp;Mathematical Foundations of Computer Science</p>

---

## Run Locally
1. Clone the repository: https://github.com/SakshiYeole/Satisfiability-using-Gentzens-Tree.git
2. Open in your favourite editor. (The editor used while making this project was VScode and also the path are currently coded to handle only windows)
3. Run the complete project by running the \source\main.py in the project directory. Follow the prompt to give input.

## Problem Statement
<p>Develop a program that takes any logical expression as input and has modules/functionalities to generate the Gentzen's Proof Tree and print whether the given expression is satisfiable or not.</p>

## Input Expression Format
1. First line is the logical expression in space separated manner.

   <details>
   <summary>Example Input Expression</summary>

   <p>( ∼ P → Q ) → ( ∼ R → S)</p>

   </details>


<p>NOTE: The input grammar should be written <a href="Input/InputGrammar.txt">here</a>.</p>

## Workflow of the code
<p>Check the main.py file to understand the flow. Following are the steps:</p>

1. Create empty output directory.
2. Take the input grammar from "InputGrammar.txt".
3. Print the input grammar to output file.
4. Compute transitions of the LR(0) automaton.
5. Compute indexing of states.
6. Compute the parsing table.
7. Print the transitions, indexing of states and parsing table to output file.