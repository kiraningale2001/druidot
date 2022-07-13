import io,os
from google.cloud import vision
import aspose.words as aw
import shutil


def detect_document(path):
    #     parent_path = 'C:\\Users\\india\\Desktop\\druidot'
    #     os.chdir(parent_path)
    """Detects document features in an image."""
    #     from google.cloud import vision
    #     import io,os
    total_word = ''
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'neon-opus-355812-dc949c4179e7.json'
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            #             print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                #                 print(paragraph)

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    total_word = total_word + ' ' + word_text
    #     print('{} '.format(
    #                         total_word))

    #                     for symbol in word.symbols:
    #                         print('\tSymbol: {} (confidence: {})'.format(
    #                             symbol.text, symbol.confidence))
    return total_word
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


n = 0
parent_path = 'C:\\Users\\india\\Desktop\\druidot'
os.chdir(parent_path)

os.mkdir('Output_image')
# adding the json file to output_image
parent_path = 'C:\\Users\\india\\Desktop\\druidot'
os.chdir(parent_path)
src_dir = os.getcwd()

dest_dir = r'C:\Users\india\Desktop\druidot\Output_image'
# gets the current working dir
print(src_dir)
dest_file = src_dir + "neon-opus-355812-dc949c4179e7.json"
shutil.move('neon-opus-355812-dc949c4179e7.json', r'C:\Users\india\Desktop\druidot\Output_image')

print(os.listdir())
# the file 'test.txt' is moved from
# src to dest with a new name

os.chdir(dest_dir)
print(os.listdir())  # list of files in dest

parent_path = 'C:\\Users\\india\\Desktop\\druidot'
os.chdir(parent_path)
os.chdir('pdf_folder')
pdf_dir = os.getcwd()
list_of_pdfs = os.listdir('.')
# os.chdir(parent_path)
for pdf in list_of_pdfs:
    doc = aw.Document(pdf)
    for page in range(0, doc.page_count):
        n += 1
        extractedPage = doc.extract_pages(page, 1)
        #         save the image file in output folder
        os.chdir(parent_path)
        os.chdir('Output_image')
        extractedPage.save(f"Output_{page + n}.jpg")
    os.chdir(parent_path)
    os.chdir(pdf_dir)
os.chdir(parent_path)
parent_path = 'C:\\Users\\india\\Desktop\\druidot'
os.chdir(parent_path)
pdf_folder = os.listdir('pdf_folder')
os.chdir(parent_path)
os.chdir('Output_image')
os.listdir()
for i in range(len(pdf_folder)):

    a = detect_document('Output_{}.jpg'.format(i + 1))
    #     print(type(a))
    try:
        f = open('file_{}.txt'.format(i + 1), 'w', encoding='utf-8')
        f.write(a)
    except Exception as e:
        print("Errorrrrrrrrr:", str(e))
    finally:
        f.close()