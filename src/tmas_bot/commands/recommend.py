"""
Book recommendation command for TMAS Academy.
"""

import discord
from discord import app_commands
from discord.ext import commands

WEBSITE_URL = "https://www.tmasacademy.com/"

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
        description="Find a TMAS Academy book for your course or subject.",
    )
    @app_commands.describe(
        book="Select the course or subject you need help with.",
        topic="Optional: describe a topic you are currently studying.",
    )
    @app_commands.choices(book=BOOK_CHOICES)
    async def recommend(
        self,
        interaction: discord.Interaction,
        book: app_commands.Choice[str],
        topic: str | None = None,
    ):
        resource = BOOKS.get(book.value)

        if resource is None:
            await interaction.response.send_message(
                "Sorry, I couldn't find that book. Please try again.",
                ephemeral=True,
            )
            return

        embed = discord.Embed(
            title="📚 Your TMAS Book Recommendation",
            description=(
                f"We recommend **{resource['title']}** "
                "for your selected course!"
            ),
            color=discord.Color.blue(),
            url=WEBSITE_URL,
        )

        embed.add_field(
            name="📖 Book",
            value=resource["title"],
            inline=False,
        )

        embed.add_field(
            name="✍️ Author(s)",
            value=resource["author"],
            inline=False,
        )

        embed.add_field(
            name="About This Book",
            value=resource["description"],
            inline=False,
        )

        embed.add_field(
            name="📊 Book Details",
            value=(
                f"**Pages:** {resource['pages']}\n"
                f"**Practice Problems:** {resource['problems']}"
            ),
            inline=True,
        )

        if topic:
            embed.add_field(
                name="🎯 Your Topic",
                value=discord.utils.escape_markdown(topic),
                inline=False,
            )

        embed.add_field(
            name="🌐 Explore TMAS Academy",
            value=f"[Visit the TMAS Academy website]({WEBSITE_URL})",
            inline=False,
        )

        embed.set_footer(
            text="TMAS Academy • Free STEM Education for Everyone"
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Recommend(bot))