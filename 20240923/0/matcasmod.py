s = int(input())
match s:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case c if (c % 2) == 0:
        print("chet")
    case n:
        print(n, "eto mnogo")
                                                                  
