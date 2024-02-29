"""
Contains the constants for the bot we are using
"""

from discord import Intents

NO_PERMS_MESSAGE = "You don't have permission to use that command."


@property
def meeting_intents():
    """static method which defines the intents for the meeting bot"""
    default_intents = Intents.default()
    default_intents.members = True
    default_intents.guilds = True
    default_intents.messages = True
    default_intents.guild_messages = True
    default_intents.message_content = True
