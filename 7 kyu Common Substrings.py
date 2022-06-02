def substring_test(s1, s2):
    pass


print(substring_test("Something","Home"), True)
print(substring_test("Something","Fun"), False)
print(substring_test("Something",""), False)
print(substring_test("","Something"), False)
print(substring_test("BANANA","banana"), True)
print(substring_test("test","lllt"), False)
print(substring_test("",""), False)
print(substring_test("1234567","541265"), True)
print(substring_test("supercalifragilisticexpialidocious","SoundOfItIsAtrocious"), True)
print(substring_test("LoremipsumdolorsitametconsecteturadipiscingelitAeneannonal"
                                  "iquetligulautplaceratorciSuspendissepotentiMorbivolutpatau"
                                  "ctoripsumegetaliquamPhasellusidmagnaelitNullamerostelluste"
                                  "mporquismolestieaornarevitaediamNullaaliquamrisusnonviverr"
                                  "asagittisInlaoreetultricespretiumVestibulumegetnullatincid"
                                  "untsempersemacrutrumfelisPraesentpurusarcutempusnecvariusi"
                                  "dultricesaduiPellentesqueultriciesjustolobortisrhoncusdign"
                                  "issimNuncviverraconsequatblanditUtbibendumatlacusactristiq"
                                  "ueAliquamimperdietnuncsempertortorefficiturviverra","thisisalongstringtest"), True)
