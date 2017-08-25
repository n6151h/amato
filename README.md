AMATO
=====

Web application for managing (small-to-midsized) opera and theatre companies.   The name is an acronym -- **A**pplication for **M**anaging **A**ll of **T**ony's **O**peras.  _Tony_ is Anthony Amato, founder of the
*[Amato Opera Theatre](https://en.wikipedia.org/wiki/Amato_Opera)*
which he started in 1948 and ran for 61 consequtive seasons.

 ![Antonio "Tony" Amato (1920-2011)](/amato/tonyback.jpg)


A Little bit of History
-----------------------

I originally started this project about ten years ago during my time with Amato Opera when Irene Kim, Tony's niece, asked if I could write a program that would help her keep track of the performance schedule.   Amato Opera was basically a school of opera and repertory company rolled into one organisation. They produced five operas each season.  Each production had 12 to 15 shows, with each show having, potentially, a different cast from any of the others.  Thus, there were many opportunities for emerging singers to learn and perform many operatic roles.  It also made scheduling all of those performances into what any normal person would call a nightmare, but what to Tony was simply magic that he more or less did in his head.

For each production, Tony producted a table (using pencil and paper) that Irene then reproduced in a Word document looking like this:


 ![Sample Amato Opera Schedule](/amato/amato-schedule.png)


Tony did this on paper and it was Irene's idea that this could somehow be automated by turning it into a spreadsheet.  The simple way to do this would be to just get Tony to learn how to use Excel or Google spreadsheet or any other kind of software.  Simple, sure.  Easy, not so much.   Tony was in his mid-80s by this time, and though he was still a very energtic 80-something (between productions he could be found high up on a tall ladder adjusting lights for the next production), he was very "old school" when it came to IT.

At around the same time, I was looking for a project I could use to teach myself java generics, and this looked to be as good as any.  The result was the original [AMATO](https://github.com/n6151h/amato-java).   This didn't use a DBMS of any sort.  Rather, it maintained everything in an XML-encoded flat file that it read in on start-up and updated when the program modified it.

Irene was beta-testing this when Tony made the decision to shut down the theatre at the start of 2009, so it was never fully-deployed.  I stopped work on it then, and it sat in my archives for several years.

Since then I've done a good bit of work with Python ORMs and web framworks (pylons, pyramid, django, sqlalchemy), and I've recently started doing more operatic work with some of the small companies around Melbourne.  Hence, I've decided to redesign AMATO as a django project.

Concepts and General Structure
-------------------------------

The project consists of several django apps: *people, library, talent,* and *schedule*.

### People and Library

At it's core, an opera company like the **Amato Opera Theatre** has a roster of artists (singers) an a repetoire of operas that it trains the singers to perform and appear in.  Scheduling amounts to matching up the singer with appropriate roles for a given performance.  Hence, the repetoire is represented in the *library* app models as subclasses of *book* (``Opera, Musical, Script``) and the artist models (``Person, Artist``) are found in the *people* app.

### Talent

Instead of having subclasses for different kinds of artists, I took a page from *Design Patterns* and made talents like singing and dancing a "has a" attribute, rather than an "is a" attribute.  Thus, an *Artist* can have one or more ``talents`` which are represented by a foreign key relationship with the *Talent* model.  This inludes numerous subclasses including ``Singer``, ``Dancer``, and so forth.

### Schedule

The schedule is where these all come together to form casts for
``Show`` instances, which are contained in ``Production`` instances.

### Season

I thought I might perhaps turn this into a website that many companies could use, each having their own libraries, artists, and schedule.  I have since decided that it is far
easier to simply run multiple sites -- perhaps hosted on the same machine -- rather than try to reinvent the wheel and manage what are effectively separate sites from within this system.

Companies organise groups of productions into *Season*s, which may or may not coincide with calendar time periods such as years or actual season (e.g. Spring).  Most companies in the US run regular seasons from September through June, say, consisting of several productions, each putting up 1 or more performances. There might also be a Summer season during which the company may take some of its repetoire on tour.  Companies in Australia, on the other hand, may have several seasons during the year, each of which including some number of perfomances of just one production.

How It Might (Eventually) Work
------------------------------

Here's a rough sketch of what the main scheduling page might look like.  THe user would select the company, season, and production from drop-down menus (indicated with the "v" on the right-hand side of the drop-down button).

  ![A rough sketch](/amato/main-idea-sketch.jpg)

The drop-downs are dynamic, populated as each of the "superior" objects are selected.  (E.g., Once **Company** is selected, the **Season** drop-down is populated for that company's seasons.  Selecting the **Season** will then populate the **Production** drop-down.)

Once a production has been selected, the grid appears.  The leftmost column lists the roles in the production's cast of characters.  Columns to the right of this will contain objects representing the actual performers for the given role.  The column heading distingquishes a particular performance (e.g. the date and/or time).  In the sketch we see that "Nick" is cast as "Nemorino" in the September 1st show, "Mia" is cast as "Adina", and so forth.

Each of the slots in these performer columns are dynnamically populated from the roster of artists.  This roster is, by default, filtered to mach the artist with specifics about the role.  For example, only tenors would be shown in any slot drop-down for "Nemorino".  There might be reasons to lift this constraint, however.  For example, "Dulcamara" is typically sung by a bass, but it could be done by a baritone as well. Thus, there should be an option to produce an unconstrained list in the performer (artist) drop-downs for this role.

### Other Stuff

We'd obviously need a bunch of other logic in this, such as the ability to add/modify/delete *Company*, *Season*, and *Production* instances.  We would also need similar management functions for *Library* and *Artist* instances, though, there is more information required for these, and the object classes are a bit more complicated.  (*Artist*s, for example, can have one or more *Talent*s in their bag of tricks.)

For simplicity, I've left out other people associated with productions like directors, set designers, choreographsers, as well as folks like conductors and stage managers for individual shows.   Furthermore, we need to pay attention to the folks in the back office who do the hard, thankless work of actually _running_ such a company, as well as the people who  work the _house_: box office and ushers.  And, let's not forget the crews: the stage hands, lighting crew, wardrobe, hair, make-up, props ... all those jobs that, sadly, no one else thinks about  or notices unless one of them does it wrong.

My aim is for a website that can manage all of this, in a way that likewise no one notices.


