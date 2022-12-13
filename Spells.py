Fireball = '''Class(es): Sorcerer, Wizard

Casting Time: 1 action
Range: 150 feet
Components: Verbal, Somatic, Material
Duration: Instantaneous

Material: A tiny ball of bat guano and sulfur.

A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame. Each creature in a 20-foot-radius sphere centered on that point must make a dexterity saving throw. A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one.

The fire spreads around corners. It ignites flammable objects in the area that aren’t being worn or carried.

At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd.'''

LightningBolt = '''Class(es): Sorcerer, Wizard

Casting Time: 1 action
Range: Self
Components: Verbal, Somatic, Material
Duration: Instantaneous

Material: A bit of fur and a rod of amber, crystal, or glass.

A stroke of lightning forming a line 100 feet long and 5 feet wide blasts out from you in a direction you choose. Each creature in the line must make a dexterity saving throw. A creature takes 8d6 lightning damage on a failed save, or half as much damage on a successful one.

The lightning ignites flammable objects in the area that aren’t being worn or carried.

At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd.'''

DayLight = '''Class(es): Cleric, Druid, Paladin, Ranger, Sorcerer

Casting Time: 1 action
Range: 60 feet
Components: Verbal, Somatic
Duration: 1 hour

A 60-foot-radius sphere of light spreads out from a point you choose within range. The sphere is bright light and sheds dim light for an additional 60 feet.

If you chose a point on an object you are holding or one that isn’t being worn or carried, the light shines from the object and moves with it. Completely covering the affected object with an opaque object, such as a bowl or a helm, blocks the light.

If any of this spell’s area overlaps with an area of darkness created by a spell of 3rd level or lower, the spell that created the darkness is dispelled.'''

MassHealingWord = '''Class(es): Cleric

Casting Time: 1 bonus action
Range: 60 feet
Components: Verbal
Duration: Instantaneous

As you call out words of restoration, up to six creatures of your choice that you can see within range regain hit points equal to 1d4 + your spellcasting ability modifier. This spell has no effect on undead or constructs.

At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, the healing increases by 1d4 for each slot level above 3rd.'''

Sending = '''Class(es): Bard, Cleric, Wizard

Casting Time: 1 action
Range: Unlimited
Components: Verbal, Somatic, Material
Duration: 1 round

Material: A short piece of fine copper wire.

You send a short message of twenty-five words or less to a creature with which you are familiar. The creature hears the message in its mind, recognizes you as the sender if it knows you, and can answer in a like manner immediately. The spell enables creatures with Intelligence scores of at least 1 to understand the meaning of your message.

You can send the message across any distance and even to other planes of existence, but if the target is on a different plane than you, there is a 5 percent chance that the message doesn’t arrive.'''

TinyHut = '''Class(es): Bard, Wizard

Casting Time: 1 minute
Range: Self
Components: Verbal, Somatic, Material
Duration: 8 hours

Material: A small crystal bead.

A 10-foot-radius immobile dome of force springs into existence around and above you and remains stationary for the duration. The spell ends if you leave its area.

Nine creatures of Medium size or smaller can fit inside the dome with you. The spell fails if its area includes a larger creature or more than nine creatures. Creatures and objects within the dome when you cast this spell can move through it freely. All other creatures and objects are barred from passing through it. Spells and other magical effects can’t extend through the dome or be cast through it. The atmosphere inside the space is comfortable and dry, regardless of the weather outside.

Until the spell ends, you can command the interior to become dimly lit or dark. The dome is opaque from the outside, of any color you choose, but it is transparent from the inside.'''

WindWall = '''Class(es): Druid, Ranger

Casting Time: 1 action
Range: 120 feet
Components: Verbal, Somatic, Material
Duration: Concentration, up to 1 minute

Material: A tiny fan and a feather of exotic origin.

A wall of strong wind rises from the ground at a point you choose within range. You can make the wall up to 50 feet long, 15 feet high, and 1 foot thick. You can shape the wall in any way you choose so long as it makes one continuous path along the ground. The wall lasts for the duration.

When the wall appears, each creature within its area must make a strength saving throw. A creature takes 3d8 bludgeoning damage on a failed save, or half as much damage on a successful one.

The strong wind keeps fog, smoke, and other gases at bay. Small or smaller flying creatures or objects can’t pass through the wall. Loose, lightweight materials brought into the wall fly upward. Arrows, bolts, and other ordinary projectiles launched at targets behind the wall are deflected upward and automatically miss. (Boulders hurled by giants or siege engines, and similar projectiles, are unaffected.) Creatures in gaseous form can’t pass through it.'''

#all spells curently entered in the dictinary are LV 3 Evocation spells
i = 0

Spells = {"fireball": Fireball, "lightning bolt": LightningBolt, "Daylight": DayLight, "mass healing word": MassHealingWord, "tiny hut": TinyHut, "wind wall": WindWall }

while True:
    #print a space before displaying dictinary items
    for keys, value in Spells.items():
        if i < 1:
            print("    ")
            i += 1
        print(keys)
        print("     ")
    
    #if it is a spell in the dictinary print the spells discription
    SpellToUse = input("what spell do you want to look at? ")
    if SpellToUse in Spells:
        print(Spells[SpellToUse])
