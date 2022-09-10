MAKEFLAGS=w

include Makefile

.PHONY: dummy_for_database_reading
dummy_for_database_reading:

EXTERNAL_LIB_OBJS = library.o

../external_lib.a: $(EXTERNAL_LIB_OBJS)
	echo $(MAKEFLAGS)
	ar crs $@ $?
