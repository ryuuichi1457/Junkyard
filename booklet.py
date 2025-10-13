from PyPDF2 import PdfReader, PdfWriter, PageObject, Transformation

# PDFを読み込む
pdf=PdfReader("sample.pdf")
writer=PdfWriter()


def make_index(p):

    res=[]
    s=[p*4-1,0]
    for i in range(2*p):
        res.append(s[1])
        res.append(s[0])
        tmp=s[((i+1)%2)]
        s[(i+1)%2]=s[i%2]-1
        s[i%2]=tmp+1

    return res[::-1]

N=len(pdf.pages)
p=((N+3)//4)#ページ数
L=make_index(p)


# 1枚目のサイズを基準にする
first_page=pdf.pages[0]
base_width=first_page.mediabox.width
base_height=first_page.mediabox.height


for i in L:

    if i<N:
        page=pdf.pages[i]
    else:
        page=PageObject.create_blank_page(width=base_width, height=base_height)
    
   
    writer.add_page(page)




with open("merged.pdf", "wb") as f:
    writer.write(f)

print("うまくいったぜ！")
print("印刷するときは、2ページ/枚、両面で「短辺綴じ」を選択してくれ！")
print("もし、元のpdfが横長だったら、表紙を折り目が上になるようにしてくれ！")