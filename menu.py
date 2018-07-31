#coding:utf-8

menu = print("1 - introduction \n2 - premier programme\n3 - variables\n4 - operations\n5 - conditions\n6 - boucles\n7 - fonctions\n8 - modularité\n9 - gestion erreurs \n10 - programmation objet \n11 - classes et attributs\n12 - méthodes\n13 -propriétés d'encapsulation\n14 - héritage\n15 - chaines de caractères")

choice = input("Choisissez votre chapitre s'il vous plait ! ")
#chapitre 1
if (choice == "1"):
    print("\nPython est un langage de programmation objet, multi-paradigme et multiplateformes. Il favorise la programmation impérative structurée, fonctionnelle et orientée objet. Il est doté d'un typage dynamique fort, d'une gestion automatique de la mémoire par ramasse-miettes et d'un système de gestion d'exceptions ; il est ainsi similaire à Perl, Ruby, Scheme, Smalltalk et Tcl.Le langage Python est placé sous une licence libre proche de la licence BSD et fonctionne sur la plupart des plates-formes informatiques, des supercalculateurs aux ordinateurs centraux, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et aussi avec Java ou encore .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser.Il est également apprécié par certains pédagogues qui y trouvent un langage où la syntaxe, clairement séparée des mécanismes de bas niveau, permet une initiation aisée aux concepts de base de la programmation. ")
    print("\nDate de première version: le 20 février 1991, il y a 27 ans\nParadigmes: Objet, impératif et interprété\nAuteur: Guido van Rossum\nDéveloppeurs: Python Software Foundation\nDernière version: 3.7.0 (27 juin 2018)  2.7.15 (1er mai 2018)\nTypage: Fort, dynamique, duck typing\nInfluencé par: ABC, C, Eiffel, ICON, Modula-3, Java, Perl, Smalltalk, Tcl\nA influencé: Ruby, Groovy, Boo, Julia\nImplémentations: CPython, Jython, IronPython, PyPy\nÉcrit en: C pour CPython, Java pour Jython, C# pour IronPython et en Python lui-même pour PyPy Système d'exploitation Multiplateforme\nLicence: Licence libre Python Software Foundation License\nSite web: www.python.org\nExtension de fichier: py, pyc, pyd, pyo et pyw")
else if (choice == "2"):
    pass
else:
    print("Un chiffre compris entre 1 et 15 et surtout pas un caractère s'il vous plait !")
pass

    

