import streamlit as st
import random
from io import BytesIO
from fpdf import FPDF
import pandas as pd

# Expanded knowledge base with more insights
knowledge_base = [
    {"thinker": "Peter Drucker", "topic": "Management by Objectives", "insight": "What gets measured gets managed. Define success in terms of contribution, not control.", "source": "The Practice of Management"},
    {"thinker": "Peter Drucker", "topic": "Knowledge Work", "insight": "The most valuable asset of a 21st-century institution will be its knowledge workers and their productivity.", "source": "Post-Capitalist Society"},
    {"thinker": "Jack Welch", "topic": "Candor", "insight": "Lack of candor blocks smart ideas, fast action, and good people leaving. Tell the truth quickly.", "source": "Winning"},
    {"thinker": "Jack Welch", "topic": "People First", "insight": "Leaders must relentlessly upgrade their team, using every encounter to evaluate, coach, and build self-confidence.", "source": "Winning"},
    {"thinker": "Peter Drucker", "topic": "Delegation", "insight": "Do not try to do everything yourself. Focus on the few areas where you can make a real difference.", "source": "The Effective Executive"},
    {"thinker": "Jack Welch", "topic": "Differentiation", "insight": "You have to face reality as it is, not as you wish it were. Differentiate A, B, and C players.", "source": "Jack: Straight from the Gut"},
    {"thinker": "Peter Drucker", "topic": "Innovation", "insight": "Systematic innovation requires the purposeful search for opportunities.", "source": "Innovation and Entrepreneurship"},
    {"thinker": "Jack Welch", "topic": "Execution", "insight": "In real life, strategy is actually very straightforward. You pick a general direction and implement like hell.", "source": "Winning"},
    {"thinker": "Peter Drucker", "topic": "Leadership", "insight": "Leadership is not magnetic personality. It is lifting a person’s vision to higher sights, raising performance to a higher standard.", "source": "The Practice of Management"},
    {"thinker": "Jack Welch", "topic": "Crisis Management", "insight": "Control your own destiny or someone else will.", "source": "Jack: Straight from the Gut"},
    {"thinker": "Peter Drucker", "topic": "Strategic Planning", "insight": "The best way to predict the future is to create it. Planning does not deal with future decisions, but with the futurity of present decisions.", "source": "Management: Tasks, Responsibilities, Practices"},
    {"thinker": "Jack Welch", "topic": "Succession Planning", "insight": "The ultimate test of leadership is the ability to create successors who can build on your legacy.", "source": "Winning"},
    {"thinker": "Peter Drucker", "topic": "Decision Making", "insight": "Making good decisions is a crucial skill at every level. A decision is a judgment. It is rarely a choice between right and wrong.", "source": "The Effective Executive"},
    {"thinker": "Jack Welch", "topic": "Vision", "insight": "Good business leaders create a vision, articulate the vision, passionately own the vision, and relentlessly drive it to completion.", "source": "Winning"},
    {"thinker": "Peter Drucker", "topic": "Effectiveness", "insight": "Efficiency is doing things right; effectiveness is doing the right things.", "source": "The Effective Executive"},
    {"thinker": "Jack Welch", "topic": "Motivation", "insight": "Celebrate success. Reward it. Recognize it. Make a big deal out of small victories.", "source": "Winning"},
    {"thinker": "Peter Drucker", "topic": "Responsibility", "insight": "Rank does not confer privilege or give power. It imposes responsibility.", "source": "The Practice of Management"},
    {"thinker": "Jack Welch", "topic": "Speed", "insight": "Speed is everything. It is the indispensable ingredient to competitiveness.", "source": "Jack: Straight from the Gut"},
    {"thinker": "Peter Drucker", "topic": "Change", "insight": "People in any organization are always attached to the obsolete. The greatest danger in times of turbulence is not the turbulence—it is to act with yesterday’s logic.", "source": "Managing in Turbulent Times"},
    {"thinker": "Jack Welch", "topic": "Simplification", "insight": "Complexity is your enemy. Any fool can make something complicated. It takes a genius to make it simple.", "source": "Winning"}
]

# Dashboard View
st.write("👈 Start by asking a question or browsing the knowledge base in the sidebar.")
st.set_page_config(layout="wide")
# st.image("https://raw.githubusercontent.com/your-username/management-guru/main/Management_Guru_Logo.png", width=150)
st.title("📊 Management Guru Dashboard")
# ... rest of code continues
