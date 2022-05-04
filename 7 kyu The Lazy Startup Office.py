def bin_rota(arr):
    pass


print(bin_rota([
    ["Bob", "Nora"],
    ["Ruby", "Carl"]]),
    ["Bob", "Nora", "Carl", "Ruby"])
print(bin_rota([["Billy"]]), ["Billy"])
print(bin_rota([["Billy", "Nancy"]]), ["Billy", "Nancy"])
print(bin_rota([
    ["Billy"],
    ["Megan"],
    ["Aki"],
    ["Arun"],
    ["Joy"]]),
    ["Billy", "Megan", "Aki", "Arun", "Joy"])
print(bin_rota([
    ["Sam", "Nina", "Tim", "Helen", "Gurpreet", "Edward", "Holly", "Eliza"],
    ["Billy", "Megan", "Aki", "Arun", "Joy", "Anish", "Lee", "Maryan"],
    ["Nick", "Josh", "Pete", "Kavita", "Daisy", "Francesca", "Alfie", "Macy"]]),
    ["Sam", "Nina", "Tim", "Helen", "Gurpreet", "Edward", "Holly", "Eliza", "Maryan", "Lee", "Anish", "Joy", "Arun",
     "Aki", "Megan", "Billy", "Nick", "Josh", "Pete", "Kavita", "Daisy", "Francesca", "Alfie", "Macy"])
print(bin_rota([
    ["Stefan", "Raj", "Marie"],
    ["Alexa", "Amy", "Edward"],
    ["Liz", "Claire", "Juan"],
    ["Dee", "Luke", "Elle"]]),
    ["Stefan", "Raj", "Marie", "Edward", "Amy", "Alexa", "Liz", "Claire", "Juan", "Elle", "Luke", "Dee"])
