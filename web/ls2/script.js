const Book = {
  title: "The Great Gatsby",
  author: "F. Scott Fitzgerald",
  method: function () {
    return this.title + " by " + this.author;
  },
};

console.log(Book.method());
