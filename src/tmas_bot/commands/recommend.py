"""
Book recommendation command for TMAS Academy.
"""

import discord
from discord import app_commands
from discord.ext import commands

WEBSITE_URL = "https://www.tmasacademy.com/"
BOOKS_URL = "https://www.tmasacademy.com/books"

BOOKS = {
    "amc-10-12-key": {
        "title": "AMC 10/12 Key Fundamentals and Strategies",
        "author": "Ritvik Rustagi",
        "pages": "25+",
        "problems": "50+",
        "description": (
            "Quick reference guide with essential formulas, strategies, "
            "and tips for AMC competitions."
        ),
    },
    "ace-amc-10-12": {
        "title": "ACE The AMC 10/12",
        "author": "Ritvik Rustagi",
        "pages": "350+",
        "problems": "300+",
        "description": (
            "Competition math strategies, problem-solving techniques, "
            "and practice problems for AMC success."
        ),
    },
    "ace-ap-calculus-ab": {
        "title": "ACE AP Calculus AB",
        "author": "Ritvik Rustagi",
        "pages": "280+",
        "problems": "150+",
        "description": (
            "Comprehensive coverage of AP Calculus AB topics with "
            "detailed explanations and practice problems."
        ),
    },
    "ace-ap-calculus-bc": {
        "title": "ACE AP Calculus BC",
        "author": "Ritvik Rustagi",
        "pages": "300+",
        "problems": "200+",
        "description": (
            "Master advanced calculus topics including series, "
            "parametric equations, and polar coordinates."
        ),
    },
    "ace-ap-physics-1": {
        "title": "ACE AP Physics 1",
        "author": "Ritvik Rustagi",
        "pages": "270+",
        "problems": "180+",
        "description": (
            "Fundamental physics concepts, problem-solving strategies, "
            "and exam preparation techniques."
        ),
    },
    "ace-ap-physics-c": {
        "title": "ACE AP Physics C: Mechanics",
        "author": "Ritvik Rustagi",
        "pages": "300+",
        "problems": "160+",
        "description": (
            "Calculus-based mechanics covering kinematics, dynamics, "
            "energy, and momentum."
        ),
    },
    "ace-ap-chemistry": {
        "title": "ACE AP Chemistry",
        "author": "Aditya Baisakh",
        "pages": "400+",
        "problems": "100+",
        "description": (
            "Thorough review of AP Chemistry topics, including "
            "practice problems and exam strategies."
        ),
    },
    "ace-ap-csp": {
        "title": "ACE AP Computer Science Principles",
        "author": "Ipsaan Sedhai, Aviva Iyerkhan",
        "pages": "100+",
        "problems": "100+",
        "description": (
            "AP Computer Science Principles study guide with clear "
            "explanations and exam-focused practice."
        ),
    },
    "ace-ap-statistics": {
        "title": "ACE AP Statistics Review Book",
        "author": "Gulshan Bhalrhu, Caden Wang",
        "pages": "200+",
        "problems": "100+",
        "description": (
            "Comprehensive coverage of statistical concepts "
            "and exam preparation."
        ),
    },
    "ace-ap-biology": {
        "title": "ACE AP Biology",
        "author": "Aditya Baisakh, Amaan Shafi, Abby Trinh",
        "pages": "300+",
        "problems": "100+",
        "description": (
            "Comprehensive coverage of AP Biology topics with "
            "detailed explanations and practice problems."
        ),
    },
    "ace-ap-psychology": {
        "title": "ACE AP Psychology",
        "author": "Sricharan Pullela, Shivek Saraf",
        "pages": "300+",
        "problems": "100+",
        "description": (
            "Comprehensive coverage of AP Psychology topics "
            "with detailed explanations and practice problems."
        ),
    },
    "ace-ap-human-geography": {
        "title": "ACE AP Human Geography",
        "author": "Shivek Saraf",
        "pages": "300+",
        "problems": "100+",
        "description": (
            "Comprehensive coverage of AP Human Geography topics "
            "with detailed explanations and practice problems."
        ),
    },
    "ace-multivariable-calculus": {
        "title": "ACE Multivariable Calculus",
        "author": "Aditya Baisakh",
        "pages": "210+",
        "problems": "100+",
        "description": (
            "Comprehensive guide covering vectors, partial derivatives, "
            "multiple integrals, and vector calculus."
        ),
    },
    "ace-differential-equations-and-linear-algebra": {
        "title": "ACE Differential Equations and Linear Algebra",
        "author": "Aditya Baisakh",
        "pages": "215+",
        "problems": "100+",
        "description": (
            "Comprehensive guide covering first-order and second-order "
            "ODEs, systems of equations, eigenvalues, eigenvectors, "
            "linear systems, and Laplace transforms."
        ),
    },
}

# Keywords used to match student topics to relevant books.
BOOK_KEYWORDS = {
    "amc-10-12-key": [
        "amc", "competition math", "math competition",
        "formulas", "quick reference",
    ],
    "ace-amc-10-12": [
        "amc", "competition math", "problem solving",
        "number theory", "combinatorics", "geometry",
    ],
    "ace-ap-calculus-ab": [
        "calculus", "limits", "derivatives", "integrals",
        "differentiation", "integration",
    ],
    "ace-ap-calculus-bc": [
        "calculus", "series", "sequences", "parametric",
        "polar", "derivatives", "integrals",
    ],
    "ace-ap-physics-1": [
        "physics", "kinematics", "forces", "motion",
        "energy", "momentum", "rotation",
    ],
    "ace-ap-physics-c": [
        "physics", "mechanics", "kinematics", "dynamics",
        "energy", "momentum", "calculus mechanics",
    ],
    "ace-ap-chemistry": [
        "chemistry", "chemical reactions", "equilibrium",
        "acids", "bases", "stoichiometry",
    ],
    "ace-ap-csp": [
        "computer science", "programming", "algorithms",
        "binary", "data", "computing",
    ],
    "ace-ap-statistics": [
        "statistics", "probability", "regression",
        "distributions", "sampling", "data analysis",
    ],
    "ace-ap-biology": [
        "biology", "cells", "genetics", "evolution",
        "organisms", "ecology",
    ],
    "ace-ap-psychology": [
        "psychology", "behavior", "memory", "cognition",
        "development", "learning",
    ],
    "ace-ap-human-geography": [
        "geography", "population", "migration",
        "urbanization", "culture", "globalization",
    ],
    "ace-multivariable-calculus": [
        "multivariable calculus", "partial derivatives",
        "multiple integrals", "vectors", "vector calculus",
        "gradients",
    ],
    "ace-differential-equations-and-linear-algebra": [
        "differential equations", "linear algebra",
        "eigenvalues", "eigenvectors", "matrices",
        "laplace transforms", "odes", "linear systems",
    ],
}

SUBJECT_CHOICES = [
    app_commands.Choice(name="AMC 10/12", value="amc"),
    app_commands.Choice(name="AP Calculus AB", value="ace-ap-calculus-ab"),
    app_commands.Choice(name="AP Calculus BC", value="ace-ap-calculus-bc"),
    app_commands.Choice(name="AP Physics 1", value="ace-ap-physics-1"),
    app_commands.Choice(name="AP Physics C: Mechanics", value="ace-ap-physics-c"),
    app_commands.Choice(name="AP Chemistry", value="ace-ap-chemistry"),
    app_commands.Choice(name="AP Computer Science Principles", value="ace-ap-csp"),
    app_commands.Choice(name="AP Statistics", value="ace-ap-statistics"),
    app_commands.Choice(name="AP Biology", value="ace-ap-biology"),
    app_commands.Choice(name="AP Psychology", value="ace-ap-psychology"),
    app_commands.Choice(name="AP Human Geography", value="ace-ap-human-geography"),
    app_commands.Choice(name="Multivariable Calculus", value="ace-multivariable-calculus"),
    app_commands.Choice(
        name="Differential Equations and Linear Algebra",
        value="ace-differential-equations-and-linear-algebra",
    ),
]


def find_recommendations(topic: str, subject: str | None = None):
    """Find books matching a student's topic and optional subject."""

    normalized_topic = topic.lower().strip()
    matches = []

    for book_id, keywords in BOOK_KEYWORDS.items():
        if subject == "amc" and not book_id.startswith(("amc-10-12", "ace-amc")):
            continue

        if subject and subject != "amc" and book_id != subject:
            continue

        score = sum(
            1 for keyword in keywords
            if keyword in normalized_topic
        )

        # Also match words from the book title.
        title_words = BOOKS[book_id]["title"].lower().split()
        score += sum(
            1 for word in title_words
            if len(word) > 3 and word in normalized_topic
        )

        if score > 0:
            matches.append((score, book_id))

    matches.sort(reverse=True)
    return [BOOKS[book_id] for _, book_id in matches]

BOOK_CHOICES = [
    app_commands.Choice(
        name="AMC 10/12 - Key Fundamentals and Strategies",
        value="amc-10-12-key",
    ),
    app_commands.Choice(
        name="AMC 10/12 - ACE The AMC 10/12",
        value="ace-amc-10-12",
    ),
    app_commands.Choice(
        name="AP Calculus AB",
        value="ace-ap-calculus-ab",
    ),
    app_commands.Choice(
        name="AP Calculus BC",
        value="ace-ap-calculus-bc",
    ),
    app_commands.Choice(
        name="AP Physics 1",
        value="ace-ap-physics-1",
    ),
    app_commands.Choice(
        name="AP Physics C: Mechanics",
        value="ace-ap-physics-c",
    ),
    app_commands.Choice(
        name="AP Chemistry",
        value="ace-ap-chemistry",
    ),
    app_commands.Choice(
        name="AP Computer Science Principles",
        value="ace-ap-csp",
    ),
    app_commands.Choice(
        name="AP Statistics",
        value="ace-ap-statistics",
    ),
    app_commands.Choice(
        name="AP Biology",
        value="ace-ap-biology",
    ),
    app_commands.Choice(
        name="AP Psychology",
        value="ace-ap-psychology",
    ),
    app_commands.Choice(
        name="AP Human Geography",
        value="ace-ap-human-geography",
    ),
    app_commands.Choice(
        name="Multivariable Calculus",
        value="ace-multivariable-calculus",
    ),
    app_commands.Choice(
        name="Differential Equations and Linear Algebra",
        value="ace-differential-equations-and-linear-algebra",
    ),
]

class Recommend(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="recommend",
        description="Find TMAS books related to a course or topic.",
    )
    @app_commands.describe(
        topic="What topic are you studying or struggling with?",
        subject="Optional: narrow your search to a specific course.",
    )
    @app_commands.choices(subject=SUBJECT_CHOICES)
    async def recommend(
        self,
        interaction: discord.Interaction,
        topic: str,
        subject: app_commands.Choice[str] | None = None,
    ):
        subject_value = subject.value if subject else None
        recommendations = find_recommendations(topic, subject_value)

        if not recommendations:
            await interaction.response.send_message(
                (
                    "I couldn't find a matching book for that topic. "
                    "Try a different keyword or select a course to narrow "
                    "your search. You can also browse the "
                    f"[TMAS Academy website]({WEBSITE_URL})."
                ),
                ephemeral=True,
            )
            return

        embed = discord.Embed(
            title="📚 Your TMAS Book Recommendations",
            description=(
                f"Here are TMAS resources related to **{topic}**."
            ),
            color=discord.Color.blue(),
            url=BOOKS_URL
        )

        for resource in recommendations[:5]:
            embed.add_field(
                name=f"📖 {resource['title']}",
                value=(
                    f"**Author(s):** {resource['author']}\n"
                    f"**Pages:** {resource['pages']}\n"
                    f"**Practice Problems:** {resource['problems']}\n"
                    f"{resource['description']}"
                ),
                inline=False,
            )

        embed.add_field(
            name="🌐 Explore TMAS Books",
            value=f"[Browse all our books!]({BOOKS_URL})",
            inline=False,
        )

        embed.set_footer(
            text="TMAS Academy • Free STEM Education for Everyone"
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Recommend(bot))