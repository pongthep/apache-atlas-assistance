from builders.rdbms.rdbms_builder_abstract import RDBMSBuilderAbstract


class PostgresqlBuilder(RDBMSBuilderAbstract):
    def __init__(self, rdbms_type: str = 'postgresql'):
        self.rdbms_type = rdbms_type
