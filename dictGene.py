import random

dictGene = {'Dicarboxylic aminoaciduria : ': 'SLC1A1',
            'Cystinuria A->rBAT : ': 'SLC3A1',
            'Cystinuria B->B0,+AT : ': 'SLC7A9',
            'Cystinosis, AR, cause inherited Fanconi\'s syndrome: ': 'CTNS',
            'dRTA effect Cl-HCO3 exchanger(AD) : ': 'SLC4A1',
            'Autosomal recessive dRTA 1: ': 'ATP6V1B1',
            'Autosomal recessive dRTA 2: ': 'ATP6V0A4',
            'Wilson disease related defect transport protein: ': 'ATP7B',
            'isolated pRTA with ocular abnormal ->NBCe1(AR) : ': 'SLC4A4',
            'Intestinal glucose-galactose malabsorption ->SGLT1 : ': 'SLC5A1',
            'Familial renal glucosuria -> SGLT2: ': 'SLC5A2',
            'Famimlial renal glycosuria : ': 'SLC5A2',
            'Hartnup\'s disorder->B0AT1  : ': 'SLC6A19',
            'Renal familial iminoglycinuria(AR) : ': 'SLC6A20',
            'Lysinuric proteir intolerance(LPI)->y+LAT1 : ': 'SLC7A7',
            'pRTA-> NHE3 mutation(AD) : ': 'SLC9A3',
            'Bartter type I -> NKCC2 : ': 'SLC12A1',
            'Gitleman -> NCC : ': 'SLC12A3',
            'Familial Renal Hypouricemia, type 1 -> URAT1 : ': 'SLC22A12',
            'Familial Renal hypouricemia, type 2 -> GLUT9 : ': 'SLC2A9',
            'Pendred Syndrome : ': 'SLC26A4',
            'Iminoglycinuria->PAT2 : ': 'SLC36A2',
            'Bartter Type II (Kir 1.1)->ROMK : ': 'KCNJ1',
            'Bartter Type I -> NKCC2: ': 'SLC12A1',
            'Bartter Type III -> CLC-Kb: ': 'CLCKB',
            'Bartter Type IV-> Barttin: ': 'BSND',
            'Bartter Type V -> CaSR: ': 'CaSR',
            'Anderson\'s Syndrome(Periodic paralysis)(Kir 2.1) : ': 'KCNJ2',
            'Familiar hyperaldosteronism(FHIII) : ': 'KCNJ5',
            'EAST Syndrome(SeSAME Syndrome)(Loss function Kir 4.1, DCT) : ': 'KCNJ10',
            'Thyrotoxic periodic paralysis (TPP)(Kir 2.6) : ': 'KCNJ18',
            'Glycinuria : ': 'SLC6A18',
            'Congenital nephrotic syndrome of the Finnish type -> nephrin : ': 'NPHS1',
            'Steroid-resistant Nephrotic syndrome -> podocin : ': 'NPHS2',
            'Sclerosteosis and it\'s milder variant, van Buchem\'s disease: ': 'SOST',
            'Isolated(nonsyndromic) diffuse mesangial sclerosis: ': 'PLCE1',
            'Hereditary hypophosphatemic rickets with hyperclaciuria: ': 'SLC34A3',
            'Autosomal recessive renal phosphate wasting: ': 'SLC34A1',
            'Autosomal recessive hypophosphatemic rickets (ARHR): ': 'DMP1&ENPP1',
            'Autosomal dominant hypophosphatemic rickets (ADHR): ': 'FGF23',
            'X-linked hypophosphatemia (XLH): ': 'PHEX',
            'Anion exchanger for oxalate secretion in intestine & PCT: ': 'SLC26A6',
            'Familial hyperaldosteronism type IV: ': 'CACNA1H',
            'Dent disease, type I, X-linked: ': 'CLCN5',
            'Dent disease, type II, X-linked: ': 'OCRL1',
            'Lowe syndrome, X-linked: ': 'OCRL1',
            'Hyperparathyroidism-Jaw tumor syndrome: ': 'HRPT2',
            'Pseudohypoparathyroidism, PHP-Ia: ': 'GNAS1',
            'MN related to which HLA antigen: ': 'HLA-DR3',
            'Anti-GBM related to which HLA antigen: ': 'HLA-DR2',
            'MCTD related to which HLA antigen: ': 'HLA-DR2,4',
            'PSGN related to which HLA antigen: ': 'HLA-DRW4',
            'Familial tumoral calcinosis: ': 'GALNT3'
            }


def list_all_disease():
    print('Your word list:\n')
    for key, value in dictGene.items():
        print('{} -> {}'.format(key, value))

def create_exam_paper():
    exam_paper = set()
# 將exam_paper設成set
    for key, value in dictGene.items():
        while len(exam_paper)<10:
            exam_paper.add(random.choice(list(dictGene.items())))
# 隨機從dictGene中取一套（key和value）並且轉換成list再加入exam_paper中，重覆做十次
    exam_paper_dict = dict(exam_paper)
# 將exam_paper從set再轉換成dict並且付值給exam_paper_dict
    return exam_paper_dict


def test_yourself():
    quit_the_test = False
    points = 0
    incorrect_gene_list = []
    exam_paper_dict = create_exam_paper()
    for key, value in exam_paper_dict.items():
        while True:
            answer = input('\nWhich gene mutation result of the disease? [p]ass, [q]uit\n{}'.format(key))
            if answer == 'p':
                print('The correct answer is {}'.format(value))
                incorrect_gene_list.append(key)
                break
            elif answer == 'q':
                quit_the_test = True
                break
            elif answer == value:
                points +=1
                print('Correct!')
                break
            else:
                print('It\'s not correct' )

        if quit_the_test == True:
            break

    print('\nScore: {}/{}'.format(points, len(exam_paper_dict)))
    print('Incorrect word list: ')
    for key in incorrect_gene_list:
        value = exam_paper_dict[key]
        print('{} ({})'.format(key, value))

    if points < 2:
        print('The brain is a good organ, but not everyone has it, right?')
    elif points >=2 and points <4 :
        print('The weather is good, right!')
    elif points >=4 and points<6 :
        print('Do more effort, you can do it!')
    elif points >=6 and points<8 :
        print('It\'s the last mile, you need to walk')
    elif points >= 8 :
        print('It\'s time to fight!!!')


def run():
    while True:
        cmd = input("""\nWelcome to my Gene dictionary
        1)Test your self!
        2)List all disease
        3)Exit\n""")
        if cmd == '1':
            test_yourself()
        if cmd == '2':
            list_all_disease()
        if cmd == '3':
            break

run()