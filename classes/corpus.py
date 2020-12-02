def get_xml_png_for_corpus(path):
    if path == None:
        path = os.path.join(PHYSCHEM, 'liion')

    cwd = os.getcwd()
    os.chdir(path)
    xml_files = glob.glob("**/sections/*/fig*.xml")
    if debug:
        print("liions ", len(liions))

    png_files = glob.glob("**/pdfimages/**/raw.png")
    if debug:
        print("liions pngs", len(liionpngs))
    os.chdir(cwd)
    return xml_files, png_files


def make_corpus_for_nltk():

    # print(liionpngs)
    maxcount = 20
    minlen = 2
    corpus =[]
    wordzz = []
    stopwords = set('oo')
    for count, liionpng in enumerate(liionpngs[:maxcount]):
        if count % 10 == 0:
            print ("img ", count, liionpng)
    #    img = Image.open(liionpng)
    #    plt.figure()
    #    plt.imshow(np.asarray(img))
    #    plt.imshow(img)

        hocr_file = os.path.join(os.path.split(liionpng)[0], 'hocr.html')
        hocr = pytesseract.image_to_pdf_or_hocr(liionpng, extension='hocr')
        with open(hocr_file, 'w+b') as f:
            f.write(hocr) # hocr
        html = open(hocr_file).read()
        htmltext = html2text.html2text(html)
        words = nltk.word_tokenize(htmltext)
        words = [word for word in words if len(word) >= minlen and not word.isnumeric()\
                and not word.lower() in stopwords]
        if len(words) > 0:
            text = " ".join(words)
        #    print("words", np.array(words))
            corpus.append(text)
            for word in words:
                wordzz.append(word)
    print("words", wordzz)
    from collections import Counter
    c = Counter(wordzz)
    print(len(c))
    print(c.most_common(20))
    print("text list", len(corpus))
    normalize_corpus = np.vectorize(corpus)
    # print(corpus)
