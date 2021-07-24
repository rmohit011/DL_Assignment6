#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2020

@author: sudhanshukumar
"""


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.preprocessing import image

model = load_model('image_tiny9.h5')

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        # load model
        model = load_model('image_tiny9.h5')

        # summarize model
        #model.summary()
        imagename = self.filename

        test_image = image.load_img(imagename, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        print(result)

       # c = pd.read_csv("category.csv")
        c={0: 'abacus',
 1: "academic gown, academic robe, judge's robe",
 2: 'acorn',
 3: 'African elephant, Loxodonta africana',
 4: 'albatross, mollymawk',
 5: 'alp',
 6: 'altar',
 7: 'American alligator, Alligator mississipiensis',
 8: 'American lobster, Northern lobster, Maine lobster, Homarus americanus',
 9: 'apron',
 10: 'Arabian camel, dromedary, Camelus dromedarius',
 11: 'baboon',
 12: 'backpack, back pack, knapsack, packsack, rucksack, haversack',
 13: 'banana',
 14: 'bannister, banister, balustrade, balusters, handrail',
 15: 'barbershop',
 16: 'barn',
 17: 'barrel, cask',
 18: 'basketball',
 19: 'bathtub, bathing tub, bath, tub',
 20: 'beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon',
 21: 'beacon, lighthouse, beacon light, pharos',
 22: 'beaker',
 23: 'bee',
 24: 'beer bottle',
 25: 'bell pepper',
 26: 'bighorn, bighorn sheep, cimarron, Rocky Mountain bighorn, Rocky Mountain sheep, Ovis canadensis',
 27: 'bikini, two-piece',
 28: 'binoculars, field glasses, opera glasses',
 29: 'birdhouse',
 30: 'bison',
 31: 'black stork, Ciconia nigra',
 32: 'black widow, Latrodectus mactans',
 33: 'boa constrictor, Constrictor constrictor',
 34: 'bow tie, bow-tie, bowtie',
 35: 'brain coral',
 36: 'brass, memorial tablet, plaque',
 37: 'broom',
 38: 'brown bear, bruin, Ursus arctos',
 39: 'bucket, pail',
 40: 'bullet train, bullet',
 41: 'bullfrog, Rana catesbeiana',
 42: 'butcher shop, meat market',
 43: 'candle, taper, wax light',
 44: 'cannon',
 45: 'cardigan',
 46: 'cash machine, cash dispenser, automated teller machine, automatic teller machine, automated teller, automatic teller, ATM',
 47: 'cauliflower',
 48: 'CD player',
 49: 'centipede',
 50: 'chain',
 51: 'chest',
 52: 'Chihuahua',
 53: 'chimpanzee, chimp, Pan troglodytes',
 54: 'Christmas stocking',
 55: 'cliff dwelling',
 56: 'cliff, drop, drop-off',
 57: 'cockroach, roach',
 58: 'comic book',
 59: 'computer keyboard, keypad',
 60: 'confectionery, confectionary, candy store',
 61: 'convertible',
 62: 'coral reef',
 63: 'cougar, puma, catamount, mountain lion, painter, panther, Felis concolor',
 64: 'crane',
 65: 'dam, dike, dyke',
 66: 'desk',
 67: 'dining table, board',
 68: "dragonfly, darning needle, devil's darning needle, sewing needle, snake feeder, snake doctor, mosquito hawk, skeeter hawk",
 69: 'drumstick',
 70: 'dugong, Dugong dugon',
 71: 'dumbbell',
 72: 'Egyptian cat',
 73: 'espresso',
 74: 'European fire salamander, Salamandra salamandra',
 75: 'flagpole, flagstaff',
 76: 'fly',
 77: 'fountain',
 78: 'freight car',
 79: 'frying pan, frypan, skillet',
 80: 'fur coat',
 81: 'gasmask, respirator, gas helmet',
 82: 'gazelle',
 83: 'German shepherd, German shepherd dog, German police dog, alsatian',
 84: 'go-kart',
 85: 'golden retriever',
 86: 'goldfish, Carassius auratus',
 87: 'gondola',
 88: 'goose',
 89: 'grasshopper, hopper',
 90: 'guacamole',
 91: 'guinea pig, Cavia cobaya',
 92: 'hog, pig, grunter, squealer, Sus scrofa',
 93: 'hourglass',
 94: 'ice cream, icecream',
 95: 'ice lolly, lolly, lollipop, popsicle',
 96: 'iPod',
 97: 'jellyfish',
 98: 'jinrikisha, ricksha, rickshaw',
 99: 'kimono',
 100: 'king penguin, Aptenodytes patagonica',
 101: 'koala, koala bear, kangaroo bear, native bear, Phascolarctos cinereus',
 102: 'Labrador retriever',
 103: 'ladybug, ladybeetle, lady beetle, ladybird, ladybird beetle',
 104: 'lakeside, lakeshore',
 105: 'lampshade, lamp shade',
 106: 'lawn mower, mower',
 107: 'lemon',
 108: 'lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens',
 109: 'lifeboat',
 110: 'limousine, limo',
 111: 'lion, king of beasts, Panthera leo',
 112: 'magnetic compass',
 113: 'mantis, mantid',
 114: 'mashed potato',
 115: 'maypole',
 116: 'meat loaf, meatloaf',
 117: 'military uniform',
 118: 'miniskirt, mini',
 119: 'monarch, monarch butterfly, milkweed butterfly, Danaus plexippus',
 120: 'moving van',
 121: 'mushroom',
 122: 'nail',
 123: 'neck brace',
 124: 'obelisk',
 125: 'oboe, hautboy, hautbois',
 126: 'orange',
 127: 'orangutan, orang, orangutang, Pongo pygmaeus',
 128: 'organ, pipe organ',
 129: 'ox',
 130: 'parking meter',
 131: 'pay-phone, pay-station',
 132: 'Persian cat',
 133: 'picket fence, paling',
 134: 'pill bottle',
 135: 'pizza, pizza pie',
 136: 'plate',
 137: "plunger, plumber's helper",
 138: 'pole',
 139: 'police van, police wagon, paddy wagon, patrol wagon, wagon, black Maria',
 140: 'pomegranate',
 141: 'poncho',
 142: 'pop bottle, soda bottle',
 143: 'potpie',
 144: "potter's wheel",
 145: 'pretzel',
 146: 'projectile, missile',
 147: 'punching bag, punch bag, punching ball, punchball',
 148: 'reel',
 149: 'refrigerator, icebox',
 150: 'remote control, remote',
 151: 'rocking chair, rocker',
 152: 'rugby ball',
 153: 'sandal',
 154: 'school bus',
 155: 'scoreboard',
 156: 'scorpion',
 157: 'sea cucumber, holothurian',
 158: 'sea slug, nudibranch',
 159: 'seashore, coast, seacoast, sea-coast',
 160: 'sewing machine',
 161: 'slug',
 162: 'snail',
 163: 'snorkel',
 164: 'sock',
 165: 'sombrero',
 166: 'space heater',
 167: "spider web, spider's web",
 168: 'spiny lobster, langouste, rock lobster, crawfish, crayfish, sea crawfish',
 169: 'sports car, sport car',
 170: 'standard poodle',
 171: 'steel arch bridge',
 172: 'stopwatch, stop watch',
 173: 'sulphur butterfly, sulfur butterfly',
 174: 'sunglasses, dark glasses, shades',
 175: 'suspension bridge',
 176: 'swimming trunks, bathing trunks',
 177: 'syringe',
 178: 'tabby, tabby cat',
 179: 'tailed frog, bell toad, ribbed toad, tailed toad, Ascaphus trui',
 180: 'tarantula',
 181: 'teapot',
 182: 'teddy, teddy bear',
 183: 'thatch, thatched roof',
 184: 'torch',
 185: 'tractor',
 186: 'trilobite',
 187: 'triumphal arch',
 188: 'trolleybus, trolley coach, trackless trolley',
 189: 'turnstile',
 190: 'umbrella',
 191: 'vestment',
 192: 'viaduct',
 193: 'volleyball',
 194: 'walking stick, walkingstick, stick insect',
 195: 'water jug',
 196: 'water tower',
 197: 'wok',
 198: 'wooden spoon',
 199: 'Yorkshire terrier'}
        for i in range(len(result[0])):
            if result[0][i] == max(result[0]):
                clas=c[i]
                print(c[i])
                pred_score=result[0][i]*100
                pred_score=str(pred_score)+"%"
                print(result[0][i])
                print(i)
                a=[{clas:pred_score}]
                return a



