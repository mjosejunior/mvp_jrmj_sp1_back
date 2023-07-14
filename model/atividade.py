from sqlalchemy import Column, Float, Integer, DateTime, Date, Time
from sqlalchemy.orm import relationship
from datetime import datetime, time
from typing import Union
import json

from model import Base, Observacao


class Atividade(Base):
    __tablename__ = 'atividade'

    id = Column("pk_atividade", Integer, primary_key=True)
    data = Column(Date, unique=True)
    start_time = Column(Time)
    end_time = Column(Time)
    duracao = Column(Float)
    publicacoes = Column(Integer)
    videos = Column(Integer)
    revisitas = Column(Integer)
    estudos = Column(Integer)
    # quantidade = Column(Integer)
    # valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre a atividade e a observação.
    # Essa relação é implicita, não está salva na tabela 'atividade',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    observacoes = relationship("Observacao", cascade="all, delete-orphan")

    def __init__(self, data: Date, start_time: Time, end_time: Time, duracao: float, publicacoes: int, videos: int, revisitas: int, estudos: int, data_insercao: Union[DateTime, None] = None):
        """
        Cria uma Atividade

        Arguments:
            data: data da atividade.
            start_time: hora de inicio da atividade.
            end_time: hora de fim da atividade.
            duracao: duração da atividade.
            publicacoes: quantidade de publicações da atividade.
            videos: quantidade de videos da atividade.
            revisitas: quantidade de revisitas da atividade.
            estudos: quantidade de estudos da atividade.

            data_insercao: data de quando a atividade foi inserida à base
        """
        self.data = data
        self.start_time = start_time
        self.end_time = end_time
        self.duracao = duracao
        self.publicacoes = publicacoes
        self.videos = videos
        self.revisitas = revisitas
        self.estudos = estudos

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_observacao(self, observacao: Observacao):
        """ Adiciona uma nova observação à atividade
        """
        self.observacoes.append(observacao)

    def to_json(self):
        return self.serializar()

    def serializar(self):
        return {
            "id": self.id,
            # Convertendo o objeto de data para string
            "data": self.data.strftime("%Y-%m-%d"),
            "start_time": self.start_time.strftime("%H:%M"),
            "end_time": self.end_time.strftime("%H:%M"),
            "duracao": self.duracao,
            "publicacoes": self.publicacoes,
            "videos": self.videos,
            "revisitas": self.revisitas,
            "estudos": self.estudos,
            # Convertendo o objeto de data e tempo para string
            "data_insercao": self.data_insercao.strftime("%Y-%m-%d %H:%M:%S")
        }

    def to_dict(self):
        return {
            "id": self.id,
            # Convertendo o objeto de data para string
            "data": self.data.strftime("%Y-%m-%d"),
            "start_time": self.start_time.strftime("%H:%M"),
            "end_time": self.end_time.strftime("%H:%M"),
            "duracao": self.duracao,
            "publicacoes": self.publicacoes,
            "videos": self.videos,
            "revisitas": self.revisitas,
            "estudos": self.estudos,
            # Convertendo o objeto de data e tempo para string
            "data_insercao": self.data_insercao.strftime("%Y-%m-%d %H:%M:%S")
        }
