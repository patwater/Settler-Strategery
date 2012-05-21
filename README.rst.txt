A couple quick scripts as part of a fun side project to build interactive analytics for Settlers of Catan.  The goal of these tools is to provide quantative rigor to important game considerations like "where should I build?" or "How long until I can build X or Y feature?" 

We will be adding more features as we hack along and welcome any and all suggestions for analytics.  The site will also ultimately support a blog and/or forum for a more qualatative discussion of game strategy.

Current files are:

monte_carlo_v1 which is a python version of the "engine" for the analytics.  Basically this simulates 10,000 iterations of a given scenario and uses that to generate probabilistic interpretations

catanalytics_v1 is the first draft of a working javascript version of said engine, using google charts to generate some quick vizualizations 

MOAR glory to come!