import main
import wikipedia
page_content = wikipedia.page("python").content
# outputs the text content of the "Parsec" page on wikipedia


TEST_KEYWORD = "help hello"

def testing():
    main.process_audio_data(TEST_KEYWORD)
    #print(page_content)

if __name__ == '__main__':
    testing()