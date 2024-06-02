import boto3
import os


def detect_text_from_image(documentPath):
    # First, we check if the file exists
    if not os.path.exists(documentPath):
        raise FileNotFoundError(f"The file {documentPath} does not exist.")

    textract = boto3.client('textract')

    # Read the file content
    with open(documentPath, 'rb') as document:
        document_bytes = document.read()

    #Analyze the document
    response = textract.detect_document_text(
        Document={'Bytes': document_bytes}
    )

    # This part is to extract the actual text from the response object
    text_content = ''
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            text_content += block['Text'] + '\n'

    return text_content


path = "resources/mito.jpg"
text = detect_text_from_image(path)
print(text)
