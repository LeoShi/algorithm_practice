class Word
  attr_reader :content

  def initialize(word)
    @content = word
  end

  def complex?
    @content.length >= 5 || vowels?
  end

  private
  def vowels?
    @content.split('').select {|char| %w(a e i o u).include?(char.downcase)}.length >= 2
  end
end
