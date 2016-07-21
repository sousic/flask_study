drop table if EXISTS entries;
create table entires (
  id INTEGER PRIMARY key autoincrement,
  title string not null,
  text string not null
);