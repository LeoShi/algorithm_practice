require_relative 'sentence'

class Page
  attr_reader :sentences, :content

  def initialize(content)
    @content = content
    @sentences= parse
  end

  def fog_index
    #Fog index = 0.4 * (words / sentence) + 100 (Complex Words / Words)
    0.4 * (words.length / sentences.length) + 100 * (complex_words.length / words.length)
  end

  def complex_words
    @sentences.inject([]) {|words, line| words + line.complex_words}
  end

  def words
    @sentences.inject([]) { |words, line| words + line.words }
  end

  private
  def parse
    @content.split("\n").select{|sentence| !sentence.strip.empty?}
                        .collect {|sentence| Sentence.new(sentence)}
  end
end
