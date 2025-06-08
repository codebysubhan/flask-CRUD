drop table if exists feedback;
create table feedback (
    id integer primary key autoincrement,
    name text not null,
    email text not null,
    subject text not null,
    message text not null
);