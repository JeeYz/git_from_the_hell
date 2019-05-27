# @Author: J.Y.
# @Date:   2019-05-27T10:29:01+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-27T14:03:20+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY



let the input be a string I consisting of n characters: a1 ... an.
let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
for each s = 1 to n
  for each unit production Rv → as
    set P[1,s,v] = true
for each l = 2 to n -- Length of span
  for each s = 1 to n-l+1 -- Start of span
    for each p = 1 to l-1 -- Partition of span
      for each production Ra  → Rb Rc
        if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
if P[n,1,1] is true then
  I is member of language
else
  I is not member of language


def make_CYK_table():
    for s in n:
        for Rv in as:
            pass
    for l in n:
        for s in n-l+1:
            for p in l-1:
                for Ra in Rb, Rc:
                    if P[p,s,b] and P[l-p, s+p, c] is True:
                        pass



    return




if __name__ == '__main__':
    print('hello, world~!')


## endl
