require_relative 'page'

FILE_NAME = 'problem.txt'


def get_file_content
  #asssume file is relatively small that can be entirely read in memory
  File.open(FILE_NAME, 'r').read
end

page = Page.new(get_file_content)

puts <<EOF
File name: #{FILE_NAME}
The fog index:#{page.fog_index},
The total number of words is #{page.words.length} and sentences in the document are #{page.sentences.length}
The average number of words per sentence is #{page.words.length / page.sentences.length}
The fog index per sentence are #{page.sentences.map(&:fog_index)}
EOF
