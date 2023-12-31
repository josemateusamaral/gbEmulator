class InstructionsSet__16BITS_ARITHMETIC:
    
    #1
    def instruction_0x09(self):  # ADD HL, BC
        self.add_to_HL(self.register_BC())

    def instruction_0x19(self):  # ADD HL, DE
        self.add_to_HL(self.register_DE())

    def instruction_0x29(self):  # ADD HL, HL
        self.add_to_HL(self.register_HL())

    def instruction_0x39(self):  # ADD HL, SP
        self.add_to_HL(self.register_SP)

    def add_to_HL(self, value):
        result = self.register_HL() + value

        # Set N flag to Reset
        self.set_flag('N', False)

        # Set H flag if carry from bit 11
        self.set_flag('H', (self.register_HL() & 0x0FFF) + (value & 0x0FFF) > 0x0FFF)

        # Set C flag if carry from bit 15
        self.set_flag('C', result > 0xFFFF)

        # Update HL with the result (16 bits)
        self.register_H = (result >> 8) & 0xFF
        self.register_L = result & 0xFF





    #2
    def instruction_0xE8(self):  # ADD SP, #
        immediate_value = self.fetch_byte()
        self.add_to_SP(immediate_value)

    def add_to_SP(self, value):
        signed_value = self.to_signed_byte(value)
        result = self.register_SP + signed_value

        # Set Z flag to Reset
        self.set_flag('Z', False)

        # Set N flag to Reset
        self.set_flag('N', False)

        # Set H flag if carry from bit 11
        self.set_flag('H', (self.register_SP & 0x0F) + (signed_value & 0x0F) > 0x0F)

        # Set C flag if carry from bit 15
        self.set_flag('C', (self.register_SP & 0xFF) + signed_value > 0xFF)

        # Update SP with the result (16 bits)
        self.register_SP = result & 0xFFFF

    def fetch_byte(self):
        opcode = self.hardware.addressedMemory[self.register_PC]
        self.register_PC += 1
        return opcode

    def to_signed_byte(self, value):
        return (value + 128) & 0xFF - 128





    #3
    def instruction_0x03(self):  # INC BC
        register_BC = self.register_BC()
        register_BC += 1
        self.register_B = (register_BC >> 8) & 0xFF
        self.register_C = register_BC & 0xFF

    def instruction_0x13(self):  # INC DE
        register_DE = self.register_DE()
        register_DE += 1
        self.register_D = (register_DE >> 8) & 0xFF
        self.register_E = register_DE & 0xFF

    def instruction_0x23(self):  # INC HL
        register_HL = self.register_HL()
        register_HL += 1
        self.register_H = (register_HL >> 8) & 0xFF
        self.register_L = register_HL & 0xFF

    def instruction_0x33(self):  # INC SP
        self.register_SP += 1



    #4
    def instruction_0x03(self):  # DEC BC
        register_BC = self.register_BC()

        register_BC -= 1
        self.register_B = (register_BC >> 8) & 0xFF
        self.register_C = register_BC & 0xFF

    def instruction_0x13(self):  # DEC DE
        register_DE = self.register_DE()
        register_DE -= 1
        self.register_D = (register_DE >> 8) & 0xFF
        self.register_E = register_DE & 0xFF

    def instruction_0x23(self):  # DEC HL
        register_HL = self.register_HL()
        register_HL -= 1
        self.register_H = (register_HL >> 8) & 0xFF
        self.register_L = register_HL & 0xFF

    def instruction_0x33(self):  # DEC SP
        self.register_SP -= 1
