# Hamburglar
Hamburglar is a utility capable of automatically comparing different versions of minecraft game
for the purpose of writing the protocol specification, interoperability, and other neat uses. The needed information is gathered with [Burger](https://github.com/TkTech/Burger) and then piped to Hamburglar.

## Usage
Currently the only way to use Hamburglar is to pipe in output from [Burger](https://github.com/TkTech/Burger)

    $ python Burger/munch.py -c minecraft.1.5.jar minecraft.1.6.jar | python Hamburglar/hamburglar.py

Hamburglar expects a JSON list conataining two objects. Using [Burger's](https://github.com/TkTech/Burger) -t option is possible as missing toppings are ignored by Hamburglar.
