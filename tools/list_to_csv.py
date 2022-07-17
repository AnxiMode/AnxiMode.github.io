ops_list = """
    1. Rain - FMA: Brotherhood (5)
    2. Colors - Code Geass (1)
    3. Hacking to the Gate - Steins;Gate
    4. Sing my Pleasure - Vivy -Fluorite Eye's Song- 
    5. World End - Code Geass (5)
    6. Departure! - Hunter x Hunter
    7. Duvet - Serial Experiments Lain
    8. Connect - Puella Magi Madoka Magica
    9. A Cruel Angel's Thesis - Neon Genesis Evangelion
    10. Period - FMA: Brotherhood (4)
    11. Tank! - Cowboy Bebop
    12. Platinum Disco - Nisemonogatari (3)
    13. Fatima - Steins;Gate 0
    14. My Soul, Your Beats! - Angel Beats!
    15. The Girls are Alright - A Place Further Than The Universe
    16. Grain - Monster
    17. Chocolate Insomnia - Nekomonogatari White
    18. Ambiguous - Kill la Kill (2)
    19. Bloody Stream - JoJo's Bizarre Adventure (2)
    20. White Lies - Onimonogatari
    21. Out of Control - Psycho-Pass (2)
    22. Let Me Hear - Parasyte -the maxim-
    23. Around the World - Initial D First Stage (1)
    24. Sugar Sweet Nightmare - Bakemonogatari (5)
    25. Mathemagics - Owarimonogatari (2)
    26. Seize the Day - Laid-Back Camp (2)
    27. Trigger - Terror in Resonance
    28. Treacherous Sunset - Durarara!! (1)
    29. Sono Chi no Sadame - JoJo's Bizarre Adventure (1)
    30. Sorario Days - Gurren Lagann
    31. Meiya Kadenrou - Katanagatari (1)
    32. Shiny Days - Laid-Back Camp (1)
    33. Golden Time Lover - FMA: Brotherhood (3)
    34. Perfect Slumbers - Nekomonogatari Black
    35. Again - FMA: Brotherhood (1)
    36. Fast Love/Kogarashi Sentiment - Koimonogatari
    37. Galaxy Anthem - Vivy -Fluorite Eye's Song- (Episode 7)
    38. We're not Alone - Rainbow
    39. My Hero - Inuyashiki
    40. Outsoar the Rainbow - Initial D Final Stage
    41. Yuudachi Houteishiki - Owarimonogatari (3)
    42. Ask DNA - Cowboy Bebop: The Movie
    43. Hyadain no Kakakata Kataomoi-C - Nichijou (1)
    44. Colorful - Puella Magi Madoka Magica: Rebellion
    45. G.P. - Great Pretender
    46. Mirai wa Bokura no Te no Naka - Kaiji (1)
    47. Happy Bite - Kabukimonogatari
    48. Fantastic Dreamer - Konosuba (1)
    49. The World - Death Note (1)
    50. Steppin' Out - Durarara!!x2 (3)
"""
eds_list = """
    1. Hunting for your Dream - Hunter x Hunter (2)
    2. Koko Kara, Koko Kara - A Place Further Than The Universe
    3. Fly Me to the Moon - Neon Genesis Evangelion
    4. Shiori - Owarimonogatari (2)
    5. Hyōri Ittai - Hunter x Hunter (5)
    6. Gate of Steiner - Steins;Gate 0 (Finale)
    7. Komm, Susser Tod - The End of Evangelion
    8. A Far Off Distance - Rainbow
    9. Sakura Nagashi - Evangelion 3.33
    10. Sayonara no Yukue - Owarimonogatari (1)
    11. Monster Without a Name - Psycho-Pass (1)
    12. Lyra - Steins;Gate 0 (Episode 8)
    13. Zzz - Nichijou (1)
    14. Magia - Puella Magi Madoka Magica (2)
    15. Fluorite Eye's Song - Vivy -Fluorite Eye's Song-
    16. Beautiful World - Evangelion 1.11, Evangelion 2.22
    17. Yake Ochinai Tsubasa - Charlotte
    18. Hanaato -Shirushi- - Hanamonogatari
    19. Kimi Ga Iru - Initial D Second Stage
    20. Ai wo Oshiete Kureta Kimi e - Inuyashiki
    21. The Great Pretender - Great Pretender
    22. Ray of Light - FMA: Brotherhood (5)
    23. Uso - FMA: Brotherhood (1)
    24. Kieru Daydream - Nekomonogatari Black
    25. World-Line - Steins;Gate 0 (2)
    26. The Real Folk Blues - Cowboy Bebop
    27. Rage your Dream - Initial D First Stage (1)
    28. Kimi no Shiranai Monogatari - Bakemonogatari
    29. Fuyubiyori - Laid-Back Camp (1)
    30. Gamble Rumble - Initial D Final Stage
    31. Blue - Cowboy Bebop (Finale)
    32. Sono Koe wo Oboeteru - Otorimonogatari / Onimonogatari
    33. Nagareboshi Kirari - Hunter x Hunter (4)
    34. Étoile et toi (+ White Edition) - Kizumonogatari
    35. Avid - 86 Eighty-Six (1)
    36. Shunkan Sentimental - FMA: Brotherhood (4)
    37. Gotta Knock a Little Harder - Cowboy Bebop: The Movie
    38. Trust Me - Durarara!! (1)
    39. All Alone with You - Psycho-Pass (2)
    40. Brave Song - Angel Beats!
    41. Gomen ne, Iiko ja Irarenai - Kill la Kill (1)
    42. Kimi no Gin no Niwa - Puella Magi Madoka Magica: Rebellion
    43. Just Awake - Hunter x Hunter (1)
    44. The Last Game - Steins;Gate 0 (1)
    45. Haru no Tonari - Laid-Back Camp (2)
    46. Minna no Peace - Gurren Lagann (2)
    47. Itsumo Kono Basho de - Steins;Gate: The Movie
    48. Roundabout - JoJo's Bizarre Adventure
    49. The Twelve Laws that Govern Time - Steins;Gate
    50. Mosaic Kakera - Code Geass (2)
"""

for line in eds_list.splitlines():
    try:
        linesplit = line[line.index(".")+2:].split("-")
        linesplit[0] = linesplit[0][:-1]
        linesplit[1] = linesplit[1][1:]
        print(",".join(linesplit))
    except Exception as e:
        print(line)
        pass