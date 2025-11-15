# Gachabits API

A library of words to be used in random generators.

Gachabits contains 600+ words. By deciding how to combine these words we can generate many kinds of things, for example clothing items, characters, food, magic weapons, spells and many more.

I mainly use Gachabits to spark creative ideas on what to draw or what to write about.

## What's Inside Gachabits?

Gachabits's core is a single JSON file that basically looks like this:

```
...
"weapons": ["sword", "bow", "crossbow", "axe", "dagger", "wand", "staff"],
"rarity": ["common", "uncommon", "rare", "mythic", "legendary"],
"jewelry": ["necklace", "earrings", "pendant", "bracelet", "ring", "hairpin"],
...
```

I wrapped this file inside a simple API so that it's easier to use.

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

### Project root

Visiting the server's root shows a list of all the word lists available inside Gachabits.

### User-friendly results

If you simply want some random entries, then choosing the **[list name] x 1** and the **[list name] x 10** options (`/gacha/user/[list name]/[results number]]`) will show the results neatly in a web page, so that you don't have to build an entire app using the raw API output.

### Checking a list's entries

By choosing the **test** option (`/test/[list name]`), the server will return all the words contained in a certain list. This is handy if you want to easily check a list's contents without having to look for the specific list inside the JSON file.

### Retrieving results through the API

By choosing the **get API link** option, you will obtain a link that follows this template: `/gacha/api/[list name]/[number of results]`

**This endpoint answers with raw data, and it's probably what you want to use if you want to build something that uses the API.**

For example, `/gacha/colors/5` will return 5 random colors.

There's a limit of 20 maximum results per API request.