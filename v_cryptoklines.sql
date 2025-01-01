CREATE VIEW v_cryptoklines AS
SELECT
    id,
    symbol,
    openTime AT TIME ZONE 'UTC' AT TIME ZONE 'GMT+2' AS openTime,
    openPrice,
    highPrice,
    lowPrice,
    closePrice,
    volume,
    closeTime AT TIME ZONE 'UTC' AT TIME ZONE 'GMT+2' AS closeTime,
    assetVolume,
    trades,
    BaseAssetVolume,
    QuoteAssetVolume
FROM
    cryptoklines;