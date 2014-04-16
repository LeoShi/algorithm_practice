require_relative 'word'

class Sentence
  attr_reader :words, :content

  def initialize(line)
    @content = line
    @words = parse
  end

  def fog_index
    #Fog index = 0.4 * (words / 1) + 100 (Complex Words / Words)
    0.4 * words.length + 100 * (complex_words.length / words.length)
  end

  def complex_words
    @words.select(&:complex?)
  end

  private
  def parse
    @content.split(' ').collect {|word| Word.new(word)}
  end
end
