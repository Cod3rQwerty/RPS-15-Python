# RPS-15-Python
Rock Paper Scissors, but with 15 options, rock, fire, scissors, snake, human, tree, wolf, sponge, paper, air, water, dragon, devil, lightning and gun. You can easily add a new option by modifying the .json file, just add it's name in the "possib" dictionary and below that add an entry for it in the dictionary, with the key being its name and value being a list with what it can beat, eg. if i wanted to add "Nuke" as an option, I would update
`"possib": ["rock", "fire", "scissors", "snake", "human",
        "tree", "wolf", "sponge", "paper", "air", "water", "dragon",
        "devil", "lightning", "gun"],`
to 
`"possib": ["rock", "fire", "scissors", "snake", "human",
        "tree", "wolf", "sponge", "paper", "air", "water", "dragon",
        "devil", "lightning", "gun", "nuke"],`
and add an entry for it in the dictionary something like:
`"Nuke": ["rock", "fire", "scissors", "snake", "human",
        "tree", "wolf", "sponge", "paper", "air", "water", "dragon",
        "devil", "lightning", "gun"],` so it can beat everything >:)
