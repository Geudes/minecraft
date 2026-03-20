from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine
)


class Database:    
    engine: AsyncEngine
    session: AsyncSession
    
    def engine(self, 
        url: str,    
        echo: bool=False
    ):
        self.engine = create_async_engine(
            url,
            echo=echo
        )

    def session(self, autoflush:bool = False):
        self.session = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            autoflush=autoflush

        )
        
        
    async def get_session(self):
        async with self.session() as session:
            try:
                yield session
                await session.flush()
            except Exception as e:
                await session.rollback()
            finally:
                await session.close()
            
