import discord
import re
import artefact_list

client = discord.Client()


# Logs the Bot in and prints a ready message to the console.
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Reads the chat and waits for commands, does something when a defined command is typed.
@client.event
async def on_message(message):
    # Ignores any messages typed by the bot itself.
    if message.author == client.user:
        return

    # !asl help - Types a "How to" to the chat, should make this a Direct message in the future.
    if message.content.startswith('!asl help'):
        await message.channel.send("""To use this bot, start your command with '!asl calc' followed by the number of 
         artefacts you have, followed by the artefact you are referencing.\nExample: 
         '!asl calc 12 Pontifex Maximus figurine'. NOTE: Artefact names ARE case sensitive, including quotes.""")

    # !asl calc - The meat of the program
    if message.content.startswith('!asl calc'):
        msg = message.content
        msg = msg[10:]  # removes '!asl calc' from the beginning of the string.
        # list of users artefacts to be calculated.
        raw_users_artifacts = msg.split(sep=",")
        # Empty list for artefact string in usable format after being striped of whitespace.
        users_artifacts = []

        # Strips the whitespace from each element in raw_users_artefacts. Appends to new list (users_artefacts).
        for users_artifact in raw_users_artifacts:
            users_artifacts.append(users_artifact.strip())

        for artefact in users_artifacts:
            # Uses regex to get quantity from start of string.
            quantity = re.search('[0-9]+', artefact)
            # Converts match type to integer.
            quantity = int(quantity.group(0))
            # Uses regex to remove leading numbers from the string.
            new_artefact = re.search('\D+.+', artefact)
            # Converts Type:match to Type:string.
            new_artefact = new_artefact.group(0)
            # Strips any leading/trailing whitespace.
            new_artefact = new_artefact.strip()

            if new_artefact not in artefact_list.artefacts:
                # Resets all materials back to 0 in prep for new calculation.
                for material in artefact_list.materials_dict:
                    artefact_list.materials_dict[material] = 0
                # If there is no match for artefact in list then this message will be sent.
                await message.channel.send(f"Sorry, {artefact} is not in the list of artefacts, please check your "
                                           f"spelling and try again. TIP: Make sure you are using '' where needed. In "
                                           f"the future this will not be necessary but until then, the quotations "
                                           f"must be the same as on the items text.")
                break

            # Check to see if remaining string is in the artefact list.
            if new_artefact in artefact_list.artefacts:
                # Runs the calculator function
                artefact_list.artefact_calc(quantity, new_artefact)

        shopping_list = "You will need to buy:\n"

        # Loops through the artefact dictionary.
        for material in artefact_list.materials_dict:

            # If the material in the dictionary is not 0 it will add the material and quantity to the shopping list
            if artefact_list.materials_dict[material] != 0:
                shopping_list = shopping_list + \
                    f"{artefact_list.materials_dict[material]} {material}\n"

        # Sends the shopping list to the channel in discord.
        await message.channel.send(shopping_list)

        # Resets all materials back to 0 in prep for new calculation.
        for material in artefact_list.materials_dict:
            artefact_list.materials_dict[material] = 0


client.run("ENTER YOUR TOKEN HERE")
