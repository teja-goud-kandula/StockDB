USE [StockDB]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [source].[bhavcopysrc](
	[SYMBOL] [nvarchar](50) NOT NULL,
	[SERIES] [nvarchar](50) NOT NULL,
	[OPEN] [float] NOT NULL,
	[HIGH] [float] NOT NULL,
	[LOW] [float] NOT NULL,
	[CLOSE] [float] NOT NULL,
	[LAST] [float] NOT NULL,
	[PREVCLOSE] [float] NOT NULL,
	[TOTTRDQTY] [bigint] NOT NULL,
	[TOTTRDVAL] [float] NOT NULL,
	[TIMESTAMP] [date] NOT NULL,
	[TOTALTRADES] [bigint] NOT NULL,
	[ISIN] [nvarchar](50) NOT NULL,
	[column14] [nvarchar](1) NULL
) ON [PRIMARY]
GO