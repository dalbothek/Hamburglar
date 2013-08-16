# Hamburglar
Hamburglar is a utility capable of automatically comparing different versions of minecraft game
for the purpose of writing the protocol specification, interoperability, and other neat uses. The needed information is gathered with [Burger](https://github.com/TkTech/Burger) and then piped to Hamburglar.

## Usage
Currently the only way to use Hamburglar is to pipe in output from [Burger](https://github.com/TkTech/Burger).<br />
I recommend using my own [fork](https://github.com/sadimusi/Burger) of Burger which adds items, packet contents and better recipes

    $ python Burger/munch.py -c minecraft.1.5.jar minecraft.1.6.jar | python Hamburglar/hamburglar.py

Hamburglar expects a JSON list containing two objects. Using [Burger's](https://github.com/TkTech/Burger) -t option is possible as missing toppings are ignored by Hamburglar.

    $ python Burger/munch.py -c -t recipes,blocks,identify minecraft.1.5.jar minecraft.1.6.jar | python Hamburglar/hamburglar.py

[Burger](https://github.com/TkTech/Burger) also offers an option to directly download the newest version of minecraft: 

    $ python Burger/munch.py -c -d minecraft.1.5.jar | python Hamburglar/hamburglar.py
