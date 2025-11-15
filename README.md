# Gachabits API

A library of words to be used in random generators.

Gachabits contains 600+ words. By deciding how to combine these words we can generate many kinds of things, for example clothing items, characters, food, magic weapons, spells and many more.

I mainly use Gachabits to spark creative ideas on what to draw or what to write about.

## Installation

This project must be run inside a Python virtual environment.

```
python3 -m venv env
. env/bin/activate
pip install Flask
```

## Starting the server

Enter the Python virtual environment with `. env/bin/activate`.

Run `flask --app gachabits run -p 3000` to start the server. This command starts the server on port 3000.

## Using the API

### What's Inside Gachabits?

Gachabits's core is a single JSON file that basically looks like this:

```
...
"weapons": ["sword", "bow", "crossbow", "axe", "dagger", "wand", "staff"],
"rarity": ["common", "uncommon", "rare", "mythic", "legendary"],
"jewelry": ["necklace", "earrings", "pendant", "bracelet", "ring", "hairpin"],
...
```

I wrapped this file inside a simple API so that it's easier to use.

### Project root

Visiting the server's root shows a list of all the word lists available inside Gachabits.

For every list, you can easily get 1 random result, 10 random results, or you can select `test` to check the entire list's contents.

### Retrieving random things

Performing a GET request following this template `/gacha/[what]/[how many]` you will obtain random entries from the API.

For example, `/gacha/colors/5` will return 5 random colors.

There's a limit of 20 maximum results per API request.