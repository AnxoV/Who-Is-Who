character(herman, [man, red_hair, bald, big_nose, brown_eyes, thick_eyebrows]).

character(maria, [woman, long_hair, hat, earrings, brown_hair, brown_eyes, small_mouth, thin_eyebrows, small_nose]).

character(claire, [woman, glasses, hat, red_hair, brown_eyes, small_mouth, small_nose]).

character(charles, [man, moustache, blonde, brown_eyes, thick_lips, big_mouth, big_ears, side_hair, small_nose]).

character(richard, [man, bald, beard, brown_eyes, big_ears, moustache, long_face, small_nose]).

character(eric, [man, blonde, cap, hat, brown_eyes, big_mouth, small_nose]).

character(alex, [man, moustache, black_hair, brown_eyes, big_mouth, thick_lips, big_ears, short_hair, small_nose]).

character(peter, [man, gray_hair, white_hair, big_nose, blue_eyes, thick_eyebrows, thick_lips, big_mouth, side_hair]).

character(philip, [man, beard, black_hair, brown_eyes, big_ears, cheeks, pink_cheeks, thin_eyebrows, short_hair, small_nose]).

character(joe, [man, glasses, blonde, brown_eyes, small_mouth, short_hair, small_nose]).

character(paul, [man, glasses, white_hair, gray_hair, brown_eyes, small_mouth, big_ears, thick_eyebrows, side_hair, small_nose]).

character(david, [man, beard, blonde, brown_eyes, big_ears, side_hair, small_nose]).

character(george, [man, sad_face, hat, white_hair, gray_hair, brown_eyes, big_mouth, small_nose]).

character(frans, [man, short_hair, thick_eyebrows, red_hair, brown_eyes, small_mouth, small_nose]).

character(alfred, [man, moustache, beard, red_hair, blue_eyes, small_mouth, big_ears, long_hair, middle_hair, small_nose]).

character(bernard, [man, brown_hair, hat, brown_eyes, small_mouth, thin_eyebrows, big_nose]).

character(bill, [man, beard, red_hair, brown_eyes, big_ears, cheeks, pink_cheeks, bald, small_mouth, small_nose]).

character(anita, [woman, long_hair, blonde, brown_eyes, small_mouth, cheeks, pink_cheeks, middle_hair, small_nose]).

character(robert, [man, sad_face, brown_hair, blue_eyes, big_ears, big_nose, side_hair, long_face, cheeks, pink_cheeks]).

character(anne, [woman, short_hair, earrings, black_hair, brown_eyes, small_mouth, big_nose]).

character(sam, [man, glasses, bald, white_hair, gray_hair, brown_eyes, small_mouth, small_nose]).

character(tom, [man, glasses, bald, black_hair, blue_eyes, small_mouth, long_face, small_nose]).

character(susan, [woman, long_hair, white_hair, gray_hair, brown_eyes, thick_lips, cheeks, pink_cheeks, small_nose, side_hair]).

character(max, [man, moustache, black_hair, brown_eyes, big_mouth, thick_lips, big_nose, big_ears, short_hair]).

character_has_property(Name, Property) :-
    character(Name, Properties),
    member(Property, Properties).

sublist( [], _ ).
sublist( [X|XS], [X|XSS] ) :- sublist( XS, XSS ).
sublist( [X|XS], [_|XSS] ) :- sublist( [X|XS], XSS ).