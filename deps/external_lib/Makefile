library.o: library.c
	$(COMPILE.c) $(OUTPUT_OPTION) $<

../external_lib.a: library.o
	$(AR) $(ARFLAGS) $@ $<
